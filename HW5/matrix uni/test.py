def like_a_gauss(mat):
	"""
	Changes mat into Reduced Row-Echelon Form.
	"""
	# Let's do forward step first.
	# at the end of this for loop, the matrix is in Row-Echelon format.
	for i in range(min(len(mat), len(mat[0]))):
		# every iteration, ignore one more row and column
		for r in range(i, len(mat)):
			# find the first row with a nonzero entry in first column
			zero_row = mat[r][i] == 0
			if zero_row:
				continue
			# swap current row with first row
			mat[i], mat[r] = mat[r], mat[i]
			# add multiples of the new first row to lower rows so lower
			# entries of first column is zero
			first_row_first_col = mat[i][i]
			for rr in range(i + 1, len(mat)):
				this_row_first = mat[rr][i]
				scalarMultiple = -1 * this_row_first / first_row_first_col
				for cc in range(i, len(mat[0])):
					mat[rr][cc] += mat[i][cc] * scalarMultiple
			break

	# At the end of the forward step
	print(mat)
	# Now reduce
	for i in range(min(len(mat), len(mat[0])) - 1, -1, -1):
		# divide last non-zero row by first non-zero entry
		first_elem_col = -1
		first_elem = -1
		for c in range(len(mat[0])):
			if mat[i][c] == 0:
				continue
			if first_elem_col == -1:
				first_elem_col = c
				first_elem = mat[i][c]
			mat[i][c] /= first_elem
		# add multiples of this row so all numbers above the leading 1 is zero
		for r in range(i):
			this_row_above = mat[r][first_elem_col]
			scalarMultiple = -1 * this_row_above
			for cc in range(len(mat[0])):
				mat[r][cc] += mat[i][cc] * scalarMultiple
		# disregard this row and continue
	print(mat)

like_a_gauss([[2,1],[6,7]])
