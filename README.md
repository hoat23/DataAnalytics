# Data Analytics

## Rewrite SQL queries in Python with Pandas

### SELECT, DISTINCT, COUNT, LIMIT

<table>
<tr>
<th> SQL </th>
<th> Python </th>
</tr>


<tr>
<td>
<pre>
SELECT name
FROM titanic_test_data
</pre>
</td>

<td>
<pre>
titanic_df["name"]
</pre>
</td>
</tr>


<tr>
<td>
<pre>
SELECT *
FROM titanic_test_data
LIMIT 5
</pre>
</td>

<td>
<pre>
titanic_df.head(5)
</pre>
</td>
</tr>


<tr>
<td>
<pre>
SELECT DISTINCT age
FROM titanic_test_data
</pre>
</td>

<td>
<pre>
titanic_df["age"].unique()
</pre>
</td>
</tr>


<tr>
<td>
<pre>
SELECT COUNT(DISTINCT age)
FROM titanic_test_data
</pre>
</td>

<td>
<pre>
len(titanic_df["age"].unique())
</pre>
</td>
</tr>


</table>

### SELECT, WHERE, OR, AND, IN (SELECT with conditions)

<table>
<tr>
<th> SQL </th>
<th> Python </th>
</tr>


<tr>
<td>
<pre>
SELECT *
FROM titanic_test_data
WHERE pclass = 1
</pre>
</td>

<td>
<pre>
titanic_df[titanic_df.pclass == 1]
</pre>
</td>
</tr>


<tr>
<td>
<pre>
SELECT *
FROM titanic_test_data
WHERE pclass = 1
OR pclass = 2
</pre>
</td>

<td>
<pre>
titanic_df[(titanic_df.pclass == 1) | 
(titanic_df.pclass == 2)]
</pre>
</td>
</tr>


<tr>
<td>
<pre>
SELECT *
FROM titanic_test_data
WHERE pclass IN (1,2)
</pre>
</td>

<td>
<pre>
titanic_df[titanic_df.pclass.isin([1,2])]
</pre>
</td>
</tr>


<tr>
<td>
<pre>
SELECT name
FROM titanic_test_data
WHERE pclass = 1 
AND gender = "male"
</pre>
</td>

<td>
<pre>
titanic_df[(titanic_df.pclass == 1) 
& (titanic_df.gender == "male")]["name"] 
</pre>
</td>
</tr>


<tr>
<td>
<pre>
SELECT name, age
FROM titanic_test_data
WHERE pclass NOT IN (1,2)
</pre>
</td>

<td>
<pre>
titanic_df[~titanic_df.pclass.isin([1,2])] 
[["name","age"]]
</pre>
</td>
</tr>


</table>

### GROUP BY, ORDER BY, COUNT

<table>
<tr>
<th> SQL </th>
<th> Python </th>
</tr>


<tr>
<td>
<pre>
SELECT
pclass,
gender,
COUNT(*)
FROM titanic_test_data
GROUP BY 1,2
</pre>
</td>

<td>
<pre>
titanic_df.groupby(["pclass","gender"]).size()
</pre>
</td>
</tr>


<tr>
<td>
<pre>
SELECT
pclass,
gender,
COUNT(*)
FROM titanic_test_data
GROUP BY 1,2
ORDER BY 3 DESC
</pre>
</td>

<td>
<pre>
titanic_df.groupby(["pclass","gender"])
.size().sort_values(ascending=False) 
</pre>
</td>
</tr>


<tr>
<td>
<pre>
SELECT
name,
pclass,
gender
FROM titanic_test_data
ORDER BY 1, 2 DESC
</pre>
</td>

<td>
<pre>
titanic_df.sort_values(["name","pclass"],
ascending=[True,False])
[["name","pclass","gender"]] 

</pre>
</td>
</tr>


<tr>
<td>
<pre>
SELECT
pclass,
gender,
SUM(fare)
FROM titanic_test_data
GROUP BY 1,2
</pre>
</td>

<td>
<pre>
titanic_df.groupby(["pclass","gender"]).sum()["fare"]
</pre>
</td>
</tr>


</table>

### MIN, MAX, MEAN, MEDIAN

<table>
<tr>
<th> SQL </th>
<th> Python </th>
</tr>


<tr>
<td>
<pre>
SELECT
MIN(age) AS min,
MAX(age) AS max,
AVG(age) AS mean,
APPROX_QUANTILES(age, 100)[OFFSET(50)] AS median
FROM titanic_test_data
</pre>
</td>

<td>
<pre>
titanic_df.agg(
{'age': ['min', 'max', 
'mean', 'median']})
</pre>
</td>
</tr>

</table>
# References
- https://www.microsoft.com/en-us/research/wp-content/uploads/2017/03/main.pdf
- https://eql.readthedocs.io/en/latest/query-guide/joins.html
