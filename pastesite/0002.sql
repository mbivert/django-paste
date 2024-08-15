-- Manually run SQL code for the 0002 migration.
BEGIN;
CREATE TABLE "new__paste_paste" (
	"id"      varchar(50) NOT NULL PRIMARY KEY,
	"content" text        NOT NULL,
	"cdate"   datetime    NOT NULL,
	"mdate"   datetime    NOT NULL
);
INSERT INTO "new__paste_paste"
		("id", "content", "cdate", "mdate")
	SELECT
		"id", "content", '2024-08-15 02:43:25.240340', '2024-08-15 02:43:25.238013'
	FROM
		"paste_paste";
DROP TABLE "paste_paste";
ALTER TABLE "new__paste_paste" RENAME TO "paste_paste";
COMMIT;
