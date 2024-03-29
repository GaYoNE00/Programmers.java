-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME
FROM(
    SELECT I.ANIMAL_ID, I.NAME, I.DATETIME AS IDATE, O.DATETIME AS ODATE 
    FROM ANIMAL_INS I, ANIMAL_OUTS O
    WHERE I.ANIMAL_ID = O.ANIMAL_ID
) A
WHERE A.IDATE>A.ODATE
ORDER BY A.IDATE ASC