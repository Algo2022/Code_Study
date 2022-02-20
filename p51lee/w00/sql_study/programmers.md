## SELECT

### all record reference
```sql
SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID;
```

### order

```sql
SELECT
ANIMAL_ID, NAME
FROM
ANIMAL_INS
ORDER BY
ANIMAL_ID;
```

```sql
SELECT
NAME, DATETIME
FROM
ANIMAL_INS
ORDER BY
ANIMAL_ID DESC;
```

```sql
SELECT
ANIMAL_ID, NAME, DATETIME
FROM
ANIMAL_INS
ORDER BY
NAME, DATETIME desc
```

### condition
```sql
SELECT
ANIMAL_ID, NAME
FROM 
ANIMAL_INS
WHERE
INTAKE_CONDITION="Sick"
```

```sql
SELECT
ANIMAL_ID, NAME
FROM
ANIMAL_INS
WHERE
NOT INTAKE_CONDITION="Aged";
```

### limit

```sql
select
name
from
animal_ins
order by
datetime
limit
1
```

## SUM, MAX, MIN

### max

```sql
select
max(datetime)
from
animal_ins
```

### min

```sql
select
min(datetime)
from
animal_ins
```

### count

```sql
select
count(*)
from
animal_ins
```

```sql
SELECT
count(distinct name) as count
FROM
animal_ins
# automatically skip "NULL"
# WHERE
# not name = "NULL"
```

## GROUP BY

```sql
SELECT
animal_type, count(*)
FROM
animal_ins
WHERE
animal_type in ("Cat", "Dog")
GROUP BY
animal_type
ORDER BY
animal_type asc
```

```sql
SELECT
name, count(name) as cnt
FROM
animal_ins
GROUP BY
NAME
HAVING
cnt > 1
ORDER BY
NAME
```

```sql
SELECT
hour(datetime) as HOUR, count(*) as COUNT
FROM
animal_outs
GROUP BY
HOUR
HAVING
HOUR >= 9 and HOUR < 20
ORDER BY
HOUR
```

```sql
WITH RECURSIVE TEMP AS(
	SELECT 0 as h
    UNION all
    SELECT h+1 from TEMP where h < 23
)

SELECT
h as HOUR, count(ANIMAL_ID) as COUNT
FROM
TEMP
LEFT OUTER JOIN
ANIMAL_OUTS
ON
HOUR(DATETIME) = TEMP.h
GROUP BY
h
ORDER BY
h
```

## IS NULL

```sql
SELECT
animal_id
FROM
animal_ins
WHERE
name is null
```

```sql
SELECT
animal_id
FROM
animal_ins
WHERE
name is not null
ORDER BY
animal_id
```

```sql
SELECT
animal_type, if(name is null, "No name", name) as name, sex_upon_intake
FROM
animal_ins
```