# DjangoPowemeterAPI

## Run app

## With Python
### Install requirements
```pycon
pip install -r requirements.txt
```

### Run server

```pycon
python manage.py runserver 
```

### Make Migrations
```pycon
python manage.py migrate
```

## Using Docker
```docker
docker-compose build
```

```docker
docker-compose run
```

#
#


## API Reference

## Swagger
```url
  /api/docs
```

#
## Powermeter Api

---
### Meters

#### Get all meters

```http
  GET /api/meter
```
---

#### Get single meter

```http
  GET /api/meter/${id}
```

| Parameter | Type      | Description                        |
|:----------|:----------|:-----------------------------------|
| `id`      | `integer` | **Required**. Id of meter to fetch |

---

#### Get single meter by code

```http
  GET /api/meter/?search=${code}
```

| Parameter | Type     | Description                       |
|:----------|:---------|:----------------------------------|
| `code`    | `string` | **Optional**. Fetch by code field |

---
#### Create meter

```http
  POST /api/meter/
```

| Parameter | Type      | Description   |
|:----------|:----------|:--------------|
| `name`    | `string`  | **Required**. |
| `code`    | `string`  | **Required**. |

---
#### Update meter

```http
  PUT /api/meter/${id}
```

| Parameter | Type      | Description                        |
|:----------|:----------|:-----------------------------------|
| `id`      | `integer` | **Required**. Id of meter to fetch |
| `name`    | `string`  | **Required**.                      |
| `code`    | `string`  | **Required**.                      |

---
#### Patch meter

```http
  PATCH /api/meter/${id}
```

| Parameter | Type      | Description                        |
|:----------|:----------|:-----------------------------------|
| `id`      | `integer` | **Required**. Id of meter to fetch |
| `name`    | `string`  | **Required**.                      |
| `code`    | `string`  | **Required**.                      |

---

#### Get delete meter

```http
  DELETE /api/meter/${id}
```

| Parameter | Type      | Description                        |
|:----------|:----------|:-----------------------------------|
| `id`      | `integer` | **Required**. Id of meter to fetch |



---
### Metrics

#### Get all metrics

```http
  GET /api/metric
```
---

#### Get single metric

```http
  GET /api/metric/${id}
```

| Parameter | Type      | Description                              |
|:----------|:----------|:-----------------------------------------|
| `id`      | `integer` | **Required**. Id of metric post to fetch |

---

#### Get metrics by code or id of meter owner

```http
  GET /api/metric/?search=${code/id}
```

| Parameter | Type      | Description                       |
|:----------|:----------|:----------------------------------|
| `code`    | `string`  | **Optional**. Fetch by code field |
| `id`      | `integer` | **Optional**. Fetch by code field |

---
#### Create metric

```http
  POST /api/metric/
```

| Parameter             | Type      | Description                                 |
|:----------------------|:----------|:--------------------------------------------|
| `consumption_meter`   | `integer` | **Required** ForeignKey Reference to Meter. |
| `kwh_consumption`     | `integer` | **Required**.                               |

---
#### Update metric

```http
  PUT /api/metric/${id}
```

| Parameter             | Type      | Description                                     |
|:----------------------|:----------|:------------------------------------------------|
| `id`      | `integer` | **Required**. Id of metric to fetch             |
| `consumption_meter`   | `integer` | **Required** ForeignKey Reference to Meter.     |
| `kwh_consumption`     | `integer` | **Required**.                                   |

---
#### Patch metric

```http
  PATCH /api/metric/${id}
```

| Parameter             | Type      | Description                                 |
|:----------------------|:----------|:--------------------------------------------|
| `id`      | `integer` | **Required**. Id of metric to fetch         |
| `consumption_meter`   | `integer` | **Required** ForeignKey Reference to Meter. |
| `kwh_consumption`     | `integer` | **Required**.                               |

---

#### Delete metric

```http
  DELETE /api/metric/${id}
```

| Parameter | Type      | Description                              |
|:----------|:----------|:-----------------------------------------|
| `id`      | `integer` | **Required**. Id of metric post to fetch |

---

### Metrics operations by meter code

#### Average metrics for a single meter

```http
  GET /api/metric/average/${code}
```

| Parameter | Type     | Description                                      |
|:----------|:---------|:-------------------------------------------------|
| `code`    | `string` | **Required**. Code of meter to fetch the metrics |

#### Max metric registered in a single meter

```http
  GET /api/metric/max/${code}
```

| Parameter | Type     | Description                                      |
|:----------|:---------|:-------------------------------------------------|
| `code`    | `string` | **Required**. Code of meter to fetch the metrics |

#### Min metric registered in a single meter

```http
  GET /api/metric/min/${code}
```

| Parameter | Type     | Description                                      |
|:----------|:---------|:-------------------------------------------------|
| `code`    | `string` | **Required**. Code of meter to fetch the metrics |

#### Total metrics for a single meter

```http
  GET /api/metric/total/${code}
```

| Parameter | Type     | Description                                      |
|:----------|:---------|:-------------------------------------------------|
| `code`    | `string` | **Required**. Code of meter to fetch the metrics |
