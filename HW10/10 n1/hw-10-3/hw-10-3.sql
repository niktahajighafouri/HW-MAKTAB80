SELECT author_name
FROM
(SELECT book_name
FROM book 
JOIN (author-book
		JOIN author 
		ON author.author_id=author-book.author_id)
ON book.book_id=author-book.book_id)
WHERE book_name='x';