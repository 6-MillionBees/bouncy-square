# Arden Boettcher
# 4/9/25
# Bouncy Square

import pygame as pg
import config as c

class Square:
  def __init__(self, pos):
    self.image = pg.image.load("DVD_VIDEO_logo.png")
    self.image = pg.transform.scale(self.image, (44, 20))
    self.og_pos = pos
    self.rect = pg.Rect(pos, (50, 50))
    self.direction = c.rand_vector()
    self.color = (255, 0, 0)

  def update(self, dt):
    self.check_pos()
    self.move(dt)

  def check_pos(self):
    if self.rect.left < 0:
      if self.rect.left < - 10:
        self.rect.left = 0
      self.direction.x *= -1
      self.color = c.rainbow(self.color, 30)
    elif self.rect.right >= c.WIDTH:
      if self.rect.right >= c.WIDTH + 10:
        self.rect.right = c.WIDTH - 1
      self.direction.x *= -1
      self.color = c.rainbow(self.color, 30)

    if self.rect.top < 0:
      if self.rect.top < -10:
        self.rect.top = 0
      self.direction.y *= -1
      self.color = c.rainbow(self.color, 30)
    elif self.rect.bottom >= c.HEIGHT:
      if self.rect.bottom >= c.HEIGHT + 10:
        self.rect.bottom = c.HEIGHT - 1
      self.direction.y *= -1
      self.color = c.rainbow(self.color, 30)

  def move(self, dt):
    self.rect.topleft += self.direction * 500 * dt

  def reset(self):
    self.rect = pg.Rect(self.og_pos, self.rect.size)
    self.direction = c.rand_vector()

  def draw(self, surface):
    pg.draw.rect(surface, self.color, self.rect)
    surface.blit(self.image, self.image.get_rect(center=self.rect.center))