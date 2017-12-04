class PaintFill(object):

	def paint_fill(self, screen, r, c, color):
		if(screen[r][c] == color): return False
		self.paint_fill_helper(screen, r, c, color)
		print(screen)

	def paint_fill_helper(self, screen, r, c, color):
		if(r < 0 or r >= len(screen) or c < 0 or c >= len(screen[0])):
			return False

		if(screen[r][c] != color):
			screen[r][c] = color
			# down
			self.paint_fill_helper(screen, r-1, c, color)

			# up
			self.paint_fill_helper(screen, r+1, c, color)
			
			# left
			self.paint_fill_helper(screen, r, c-1, color)

			# right
			self.paint_fill_helper(screen, r, c+1, color)
		return True

a = PaintFill()
print(a.paint_fill([[1, 1, 2],[1, 1, 1],[1, 1, 1]], 1, 1, 2))
			