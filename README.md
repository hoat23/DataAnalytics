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


https://www.microsoft.com/en-us/research/wp-content/uploads/2017/03/main.pdf
