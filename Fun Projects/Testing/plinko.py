import json
import os
import random
import sys

import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ACCOUNTS_FILE = os.path.join(BASE_DIR, "accounts.json")

STARTING_BALANCE = 100
SCREEN_SIZE = (760, 900)
FPS = 60
BOTTOM_PANEL_HEIGHT = 160
POCKET_AREA_TOP = SCREEN_SIZE[1] - BOTTOM_PANEL_HEIGHT - 170

POCKETS = [
    {"label": "BUST", "color": (80, 80, 120), "multiplier": 0.0},
    {"label": "1x", "color": (60, 150, 80), "multiplier": 1.0},
    {"label": "2x", "color": (40, 120, 220), "multiplier": 2.0},
    {"label": "5x", "color": (240, 180, 40), "multiplier": 5.0},
    {"label": "10x", "color": (220, 70, 70), "multiplier": 10.0},
    {"label": "5x", "color": (240, 180, 40), "multiplier": 5.0},
    {"label": "2x", "color": (40, 120, 220), "multiplier": 2.0},
    {"label": "1x", "color": (60, 150, 80), "multiplier": 1.0},
    {"label": "BUST", "color": (80, 80, 120), "multiplier": 0.0},
]


def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return {"users": {}}

    try:
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (json.JSONDecodeError, OSError):
        return {"users": {}}


def save_accounts(accounts):
    try:
        with open(ACCOUNTS_FILE, "w", encoding="utf-8") as handle:
            json.dump(accounts, handle, indent=2)
    except OSError:
        pass


class InputBox:
    def __init__(self, rect, font, placeholder="", hidden=False, char_filter=None):
        self.rect = pygame.Rect(rect)
        self.font = font
        self.text = ""
        self.active = False
        self.placeholder = placeholder
        self.hidden = hidden
        self.char_filter = char_filter

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self.active = False
            elif event.key == pygame.K_TAB:
                pass
            elif event.unicode.isprintable() and (self.char_filter is None or self.char_filter(event.unicode)):
                self.text += event.unicode

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self, screen):
        color = (240, 240, 240) if self.active else (210, 210, 210)
        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        pygame.draw.rect(screen, (50, 50, 60), self.rect, 2, border_radius=12)
        display = "" if self.text == "" else ("*" * len(self.text) if self.hidden else self.text)
        if not display:
            label = self.font.render(self.placeholder, True, (120, 120, 140))
        else:
            label = self.font.render(display, True, (15, 15, 25))
        screen.blit(label, (self.rect.x + 14, self.rect.y + self.rect.height // 2 - label.get_height() // 2))


class Button:
    def __init__(self, rect, text, font, bg=(40, 120, 220), fg=(255, 255, 255)):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.bg = bg
        self.fg = fg

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg, self.rect, border_radius=14)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2, border_radius=14)
        label = self.font.render(self.text, True, self.fg)
        screen.blit(label, (self.rect.centerx - label.get_width() // 2, self.rect.centery - label.get_height() // 2))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


class Peg(pygame.sprite.Sprite):
    def __init__(self, x, y, radius=10):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (230, 220, 120), (radius, radius), radius)
        pygame.draw.circle(self.image, (190, 140, 180), (radius, radius), radius - 4)
        self.rect = self.image.get_rect(center=(x, y))
        self.pos = pygame.Vector2(x, y)


class Chip(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        size = 30
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        for index, color in enumerate([(230, 90, 80), (250, 150, 90), (255, 220, 120)]):
            pygame.draw.circle(self.image, color, (size // 2, size // 2), size // 2 - index * 4)
        pygame.draw.circle(self.image, (255, 255, 255), (size // 2, size // 2), 8)
        self.rect = self.image.get_rect(center=(x, y))
        self.pos = pygame.Vector2(self.rect.center)
        self.vel = pygame.Vector2(0, 0)
        self.radius = size // 2 - 2
        self.active = False
        self.multiplier = 0.0

    def launch(self, x):
        self.pos = pygame.Vector2(x, 60)
        self.vel = pygame.Vector2(random.choice([-40, 40]), 120)
        self.active = True
        self.multiplier = 0.0
        self.rect.center = self.pos

    def update(self, dt, pegs, width, height):
        if not self.active:
            return None

        self.vel.y += 220 * dt
        self.pos += self.vel * dt

        for peg in pegs:
            offset = self.pos - peg.pos
            distance = offset.length()
            if distance and distance < self.radius + peg.radius:
                normal = offset.normalize()
                self.vel = self.vel.reflect(normal) * 0.95
                correction = normal * ((self.radius + peg.radius) - distance + 1)
                self.pos += correction
                if abs(self.vel.y) < 50:
                    self.vel.y = 50 if self.vel.y >= 0 else -50

        if self.pos.x < 50:
            self.pos.x = 50
            self.vel.x *= -0.85
        if self.pos.x > width - 50:
            self.pos.x = width - 50
            self.vel.x *= -0.85

        self.rect.center = self.pos

        if self.pos.y >= POCKET_AREA_TOP:
            self.active = False
            bucket_index = min(max(int((self.pos.x - 30) // ((width - 60) / len(POCKETS))), 0), len(POCKETS) - 1)
            self.multiplier = POCKETS[bucket_index]["multiplier"]
            return self.multiplier

        return None


def draw_background(screen):
    for i in range(SCREEN_SIZE[1] // 12):
        color = (18 + i // 3, 18 + i // 2, 50 + i // 4)
        pygame.draw.rect(screen, color, (0, i * 12, SCREEN_SIZE[0], 12))
    pygame.draw.rect(screen, (20, 25, 35), (20, 32, SCREEN_SIZE[0] - 40, SCREEN_SIZE[1] - 64), border_radius=28)


def draw_board(screen, font):
    board_rect = pygame.Rect(30, 100, SCREEN_SIZE[0] - 60, SCREEN_SIZE[1] - BOTTOM_PANEL_HEIGHT - 140)
    pygame.draw.rect(screen, (35, 40, 60), board_rect, border_radius=22)
    pygame.draw.rect(screen, (110, 135, 180), board_rect, 4, border_radius=22)

    for x in range(70, SCREEN_SIZE[0] - 70, 120):
        pygame.draw.line(screen, (140, 160, 200), (x, 340), (x, SCREEN_SIZE[1] - BOTTOM_PANEL_HEIGHT - 80), 2)

    pocket_width = (SCREEN_SIZE[0] - 60) / len(POCKETS)
    for index, pocket in enumerate(POCKETS):
        pocket_rect = pygame.Rect(30 + pocket_width * index, SCREEN_SIZE[1] - BOTTOM_PANEL_HEIGHT - 170, pocket_width - 4, 120)
        pygame.draw.rect(screen, pocket["color"], pocket_rect, border_radius=10)
        label = font.render(pocket["label"], True, (255, 255, 255))
        screen.blit(label, (pocket_rect.centerx - label.get_width() // 2, pocket_rect.y + 14))
        win = pocket["multiplier"]
        line = font.render(f"x{win:.0f}" if win else "0x", True, (240, 240, 240))
        screen.blit(line, (pocket_rect.centerx - line.get_width() // 2, pocket_rect.y + 46))

    pygame.draw.rect(screen, (100, 100, 140), (50, SCREEN_SIZE[1] - 160, SCREEN_SIZE[0] - 100, 6))


def build_pegs():
    rows = []
    peg_bottom = POCKET_AREA_TOP - 60
    for row_index, y in enumerate(range(180, peg_bottom, 70)):
        row = []
        offset = 50 if row_index % 2 else 80
        for x in range(offset, SCREEN_SIZE[0] - offset, 100):
            row.append(Peg(x, y, radius=10))
        rows.extend(row)
    return pygame.sprite.Group(rows)


def draw_header(screen, font, title, subtext, balance, username):
    header_rect = pygame.Rect(50, 20, SCREEN_SIZE[0] - 100, 96)
    pygame.draw.rect(screen, (28, 34, 55), header_rect, border_radius=18)
    pygame.draw.rect(screen, (120, 170, 255), header_rect, 3, border_radius=18)
    title_text = font.render(title, True, (245, 245, 255))
    screen.blit(title_text, (header_rect.x + 16, header_rect.y + 10))
    sub_font = pygame.font.SysFont("arial", 20)
    info_text = sub_font.render(subtext, True, (170, 190, 215))
    screen.blit(info_text, (header_rect.x + 16, header_rect.y + 46))
    balance_text = sub_font.render(f"Balance: ${balance:,.2f}", True, (255, 215, 115))
    screen.blit(balance_text, (header_rect.right - balance_text.get_width() - 18, header_rect.y + 10))
    display_name = username if len(username) <= 14 else username[:11] + "..."
    user_text = sub_font.render(f"Player: {display_name}", True, (175, 215, 255))
    screen.blit(user_text, (header_rect.right - user_text.get_width() - 18, header_rect.y + 38))


def authenticate_user(accounts, username, password, create_new=False):
    username = username.strip()
    if username == "" or password == "":
        return False, "Username and password cannot be empty."

    user_record = accounts["users"].get(username)
    if user_record is None:
        if create_new:
            accounts["users"][username] = {"password": password, "balance": STARTING_BALANCE}
            save_accounts(accounts)
            return True, "Account created. Welcome to the Plinko Casino!"
        return False, "User not found. Create an account to play."

    if user_record["password"] != password:
        return False, "Password incorrect. Try again."

    return True, "Signed in successfully."


def parse_bet_amount(text):
    try:
        amount = float(text)
        if amount <= 0:
            return None
        return amount
    except ValueError:
        return None


def draw_login(screen, font, username_box, password_box, buttons, message):
    draw_background(screen)
    title = font.render("Plinko Casino Sign In", True, (255, 240, 210))
    screen.blit(title, (SCREEN_SIZE[0] // 2 - title.get_width() // 2, 80))
    small = pygame.font.SysFont("arial", 24)
    prompt = small.render("Use a name and password to sign in or create an account.", True, (200, 220, 255))
    screen.blit(prompt, (SCREEN_SIZE[0] // 2 - prompt.get_width() // 2, 128))
    username_box.draw(screen)
    password_box.draw(screen)
    for button in buttons:
        button.draw(screen)
    if message:
        hint = small.render(message, True, (255, 180, 80))
        screen.blit(hint, (SCREEN_SIZE[0] // 2 - hint.get_width() // 2, 560))


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Plinko Casino")
    clock = pygame.time.Clock()

    accounts = load_accounts()
    username_box = InputBox((210, 260, 340, 52), pygame.font.SysFont("arial", 28), "Username")
    password_box = InputBox((210, 340, 340, 52), pygame.font.SysFont("arial", 28), "Password", hidden=True)
    sign_in_button = Button((210, 430, 160, 52), "Sign In", pygame.font.SysFont("arial", 26))
    create_button = Button((390, 430, 160, 52), "New Account", pygame.font.SysFont("arial", 26), bg=(100, 200, 140))
    drop_button = Button((300, 760, 200, 52), "Drop Chip", pygame.font.SysFont("arial", 26), bg=(220, 120, 90))

    state = "login"
    message = ""
    current_user = None
    balance = 0.0
    bet = 10.0
    bet_box = InputBox((40, SCREEN_SIZE[1] - BOTTOM_PANEL_HEIGHT + 20, 220, 52), pygame.font.SysFont("arial", 28), "Bet amount", char_filter=lambda c: c.isdigit() or c == ".")
    bet_box.text = f"{bet:.2f}"
    selected_x = SCREEN_SIZE[0] // 2
    chip = Chip(selected_x, 60)
    pegs = build_pegs()
    result_text = ""
    result_color = (255, 255, 255)

    title_font = pygame.font.SysFont("arial", 34, bold=True)
    small_font = pygame.font.SysFont("arial", 22)
    large_font = pygame.font.SysFont("arial", 40, bold=True)

    def place_chip():
        nonlocal balance, result_text, result_color, bet
        desired_bet = parse_bet_amount(bet_box.text)
        if desired_bet is None:
            result_text = "Enter a valid bet amount."
            result_color = (235, 90, 90)
            return False
        if desired_bet > balance:
            result_text = "Not enough balance to place that bet."
            result_color = (235, 90, 90)
            return False
        bet = desired_bet
        balance -= bet
        chip.launch(selected_x)
        result_text = ""
        return True

    while True:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if current_user:
                    accounts["users"][current_user]["balance"] = balance
                    save_accounts(accounts)
                pygame.quit()
                sys.exit()

            if state == "login":
                username_box.handle_event(event)
                password_box.handle_event(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if sign_in_button.clicked(event.pos):
                        success, message = authenticate_user(accounts, username_box.text, password_box.text)
                        if success:
                            current_user = username_box.text.strip()
                            balance = accounts["users"][current_user]["balance"]
                            state = "lobby"
                            message = "Welcome back! Choose a bet and drop your chip."
                    if create_button.clicked(event.pos):
                        success, message = authenticate_user(accounts, username_box.text, password_box.text, create_new=True)
                        if success:
                            current_user = username_box.text.strip()
                            balance = accounts["users"][current_user]["balance"]
                            state = "lobby"
                            message = "Account created! You have $100 to start."
            else:
                bet_box.handle_event(event)
                if event.type == pygame.KEYDOWN and not bet_box.active:
                    if event.key == pygame.K_LEFT:
                        selected_x = max(80, selected_x - 34)
                    elif event.key == pygame.K_RIGHT:
                        selected_x = min(SCREEN_SIZE[0] - 80, selected_x + 34)
                    elif event.key == pygame.K_SPACE and not chip.active:
                        place_chip()
                    elif event.key == pygame.K_UP:
                        bet = min(balance, bet + 5)
                        bet_box.text = f"{bet:.2f}"
                    elif event.key == pygame.K_DOWN:
                        bet = max(1, bet - 5)
                        bet_box.text = f"{bet:.2f}"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 40 < event.pos[0] < SCREEN_SIZE[0] - 40 and event.pos[1] < 120:
                        selected_x = min(max(80, event.pos[0]), SCREEN_SIZE[0] - 80)
                    if event.button == 1 and not chip.active:
                        if drop_button.clicked(event.pos):
                            place_chip()

        if state == "login":
            draw_login(screen, title_font, username_box, password_box, [sign_in_button, create_button], message)
        else:
            draw_background(screen)
            draw_header(screen, title_font, "Plinko Casino", "Choose your drop zone and spin the board.", balance, current_user)
            draw_board(screen, small_font)

            for peg in pegs:
                screen.blit(peg.image, peg.rect)

            if chip.active:
                result = chip.update(dt, pegs, SCREEN_SIZE[0], SCREEN_SIZE[1])
                screen.blit(chip.image, chip.rect)
                if result is not None:
                    winnings = bet * result
                    balance += winnings
                    accounts["users"][current_user]["balance"] = balance
                    save_accounts(accounts)
                    if result == 0:
                        result_text = f"Bust! You lost ${bet:.2f}."
                        result_color = (220, 110, 90)
                    else:
                        result_text = f"Win! ${bet:.2f} x {result:.0f} = ${winnings:.2f}."
                        result_color = (160, 240, 130)
            else:
                shadow = pygame.Surface((24, 24), pygame.SRCALPHA)
                pygame.draw.circle(shadow, (255, 255, 255, 50), (12, 12), 12)
                screen.blit(shadow, (selected_x - 12, 60 - 12))
                pygame.draw.circle(screen, (255, 100, 100), (selected_x, 60), 12)
                pygame.draw.circle(screen, (255, 230, 150), (selected_x, 60), 4)

            result_y = SCREEN_SIZE[1] - BOTTOM_PANEL_HEIGHT - 60
            if result_text:
                result_render = large_font.render(result_text, True, result_color)
                screen.blit(result_render, (SCREEN_SIZE[0] // 2 - result_render.get_width() // 2, result_y))

            panel_rect = pygame.Rect(20, SCREEN_SIZE[1] - BOTTOM_PANEL_HEIGHT - 10, SCREEN_SIZE[0] - 40, BOTTOM_PANEL_HEIGHT)
            pygame.draw.rect(screen, (28, 34, 55), panel_rect, border_radius=22)
            pygame.draw.rect(screen, (105, 125, 170), panel_rect, 3, border_radius=22)

            bet_box.draw(screen)
            bet_text = title_font.render(f"Bet: ${bet_box.text or f'{bet:.2f}'}", True, (255, 235, 190))
            screen.blit(bet_text, (280, SCREEN_SIZE[1] - BOTTOM_PANEL_HEIGHT + 28))
            helper_text = small_font.render("Type your bet, or use up/down arrows to adjust.", True, (210, 220, 240))
            screen.blit(helper_text, (40, SCREEN_SIZE[1] - BOTTOM_PANEL_HEIGHT + 88))
            balance_hint = small_font.render("Space or press Drop Chip to launch. Balance saves automatically.", True, (190, 215, 240))
            screen.blit(balance_hint, (40, SCREEN_SIZE[1] - BOTTOM_PANEL_HEIGHT + 114))

            drop_button.rect.center = (SCREEN_SIZE[0] - 160, SCREEN_SIZE[1] - BOTTOM_PANEL_HEIGHT + 80)
            drop_button.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
