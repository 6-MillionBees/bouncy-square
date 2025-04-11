# Arden Boettcher
# 4/9/25
# Bouncy Square

import pygame as pg
import config as c

class Square:
  def __init__(self, pos):
    self.image = pg.image.load("DVD_VIDEO_logo.png")
    self.image = pg.transform.scale(self.image, (132, 60))
    self.og_pos = pos
    self.rect = pg.Rect(pos, (150, 150))
    self.direction = c.rand_vector()
    self.color = (255, 0, 0)
    self.flinging = False
    self.og_mouse_pos = (0, 0)
    self.line_start_pos = (-1, -1)
    self.line_end_pos = (-2, -2)
    self.reverse_pos = (-2, -2)

  def update(self, dt):
    self.check_pos()
    self.move(dt)

  def check_pos(self):
    screen_size = pg.display.get_window_size()
    if self.rect.left < 0:
      if self.rect.left < - 1:
        self.rect.left = 0
      self.direction.x *= -1
      self.color = c.rainbow(self.color, 30)
    elif self.rect.right >= screen_size[0]:
      if self.rect.right >= screen_size[0] + 1:
        self.rect.right = screen_size[0] - 1
      self.direction.x *= -1
      self.color = c.rainbow(self.color, 30)

    if self.rect.top < 0:
      if self.rect.top < -1:
        self.rect.top = 0
      self.direction.y *= -1
      self.color = c.rainbow(self.color, 30)
    elif self.rect.bottom >= screen_size[1]:
      if self.rect.bottom >= screen_size[1] + 1:
        self.rect.bottom = screen_size[1] - 1
      self.direction.y *= -1
      self.color = c.rainbow(self.color, 30)

  def move(self, dt):
    self.rect.topleft += self.direction * 500 * dt

  def reset(self):
    screen_size = pg.display.get_window_size()
    self.rect = pg.Rect((screen_size[0] / 2, screen_size[1] / 2), self.rect.size)
    self.direction = c.rand_vector()

  def events(self, event):
    if event.type == pg.MOUSEBUTTONDOWN:
      self.reset()
      self.line_start_pos = self.rect.center
      self.direction = pg.Vector2(0, 0)
      self.flinging = True
      self.og_mouse_pos = event.pos
      mouse_pos = pg.mouse.get_pos()
      self.reverse_pos = (-1 * (mouse_pos[0] - self.og_mouse_pos[0]), -1 * (mouse_pos[1] - self.og_mouse_pos[1]))
      self.line_end_pos = (self.reverse_pos[0] + self.line_start_pos[0], self.reverse_pos[1] + self.line_start_pos[1])

    elif event.type == pg.MOUSEBUTTONUP:
      speed = c.find_dist((0, 0), self.reverse_pos) / 100

      self.direction = pg.Vector2(self.reverse_pos)
      self.direction.scale_to_length(speed)
      self.line_start_pos = (-1, -1)
      self.og_mouse_pos = (0, 0)
      self.reverse_pos = (-2, -2)
      self.flinging = False


    elif event.type == pg.MOUSEMOTION:
      if self.flinging:
        mouse_pos = pg.mouse.get_pos()
        self.reverse_pos = (-1 * (mouse_pos[0] - self.og_mouse_pos[0]), -1 * (mouse_pos[1] - self.og_mouse_pos[1]))
        self.line_end_pos = (self.reverse_pos[0] + self.line_start_pos[0], self.reverse_pos[1] + self.line_start_pos[1])

  def draw(self, surface):

    if self.flinging:
      pg.draw.line(surface, self.color, self.line_start_pos, self.line_end_pos, 3)

      # slope = c.find_slope(self.line_start_pos, self.line_end_pos)
      # if slope == None:
      #   reverse_slope = 0
      # elif not slope:
      #   reverse_slope
      # else:

      # pg.draw.polygon(
      #   surface,
      #   self.color,
      #   []
      # )

    pg.draw.rect(surface, self.color, self.rect)
    surface.blit(self.image, self.image.get_rect(center=self.rect.center))
