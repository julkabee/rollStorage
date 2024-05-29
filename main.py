from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import FastAPI

from connect import engine
from models import Rolls

app = FastAPI()


# Добавление рулона на склад
@app.get("/add_data")
def add_data(length, weight):
    try:
        with Session(autoflush=False, bind=engine) as db:
            roll = Rolls(weight=weight, length=length, add_dt=datetime.now())
            db.add(roll)
            db.commit()
            roll_data = {
                "ID": roll.id,
                "length": roll.length,
                "weight": roll.weight,
                "add_dt": roll.add_dt,
                "del_dt": roll.del_dt
            }
            return roll_data
    except Exception as e:
        print(f"Error: {e}")


# Удаление рулона со склада
@app.get("/del_data")
def del_data(roll_id):
    try:
        with Session(autoflush=False, bind=engine) as db:
            f = Rolls.id == int(roll_id)
            roll = db.query(Rolls).filter(f).first()
            roll.del_dt = datetime.now()
            db.commit()
            roll_data = {
                "ID": roll.id,
                "length": roll.length,
                "weight": roll.weight,
                "add_dt": roll.add_dt,
                "del_dt": roll.del_dt
            }
            return roll_data
    except Exception as e:
        print(f"Error: {e}")


# Фильтрация рулонов по id
@app.get("/filter_id")
def filter_id(id_down, id_up):
    try:
        with Session(autoflush=False, bind=engine) as db:
            f = Rolls.id.between(id_down, id_up)
            rolls = db.query(Rolls).filter(f)
            rolls_data = []
            for roll in rolls:
                roll_data = {
                    "ID": roll.id,
                    "weight": roll.weight,
                    "add_dt": roll.add_dt,
                    "del_dt": roll.del_dt
                }
                rolls_data.append(roll_data)
            return rolls_data
    except Exception as e:
        print(f"Error: {e}")


# Фильтрация рулонов по длине
@app.get("/filter_length")
def filter_length(length_down, length_up):
    try:
        with Session(autoflush=False, bind=engine) as db:
            f = Rolls.length.between(length_down, length_up)
            rolls = db.query(Rolls).filter(f)
            rolls_data = []
            for roll in rolls:
                roll_data = {
                    "ID": roll.id,
                    "length": roll.length,
                    "weight": roll.weight,
                    "add_dt": roll.add_dt,
                    "del_dt": roll.del_dt
                }
                rolls_data.append(roll_data)
            return rolls_data
    except Exception as e:
        print(f"Error: {e}")


# Фильтрация рулонов по весу
@app.get("/filter_weight")
def filter_weight(weight_down, weight_up):
    try:
        with Session(autoflush=False, bind=engine) as db:
            f = Rolls.weight.between(weight_down, weight_up)
            rolls = db.query(Rolls).filter(f)
            rolls_data = []
            for roll in rolls:
                roll_data = {
                    "ID": roll.id,
                    "length": roll.length,
                    "weight": roll.weight,
                    "add_dt": roll.add_dt,
                    "del_dt": roll.del_dt,
                }
                rolls_data.append(roll_data)
            return rolls_data
    except Exception as e:
        print(f"Error: {e}")


# Фильтрация рулонов по дате добавления
@app.get("/filter_add_dt")
def filter_add_dt(add_dt_down, add_dt_up):
    try:
        with Session(autoflush=False, bind=engine) as db:
            f = Rolls.add_dt.between(add_dt_down, add_dt_up)
            rolls = db.query(Rolls).filter(f)
            rolls_data = []
            for roll in rolls:
                roll_data = {
                    "ID": roll.id,
                    "length": roll.length,
                    "weight": roll.weight,
                    "add_dt": roll.add_dt,
                    "del_dt": roll.del_dt
                }
                rolls_data.append(roll_data)
            return rolls_data
    except Exception as e:
        print(f"Error: {e}")


# Фильтрация рулонов по дате удаления
@app.get("/filter_del_dt")
def filter_del_dt(del_dt_down, del_dt_up):
    try:
        with Session(autoflush=False, bind=engine) as db:
            f = Rolls.del_dt.between(del_dt_down, del_dt_up)
            rolls = db.query(Rolls).filter(f)
            rolls_data = []
            for roll in rolls:
                roll_data = {
                    "ID": roll.id,
                    "length": roll.length,
                    "weight": roll.weight,
                    "add_dt": roll.add_dt,
                    "del_dt": roll.del_dt
                }
                rolls_data.append(roll_data)
            return rolls_data
    except Exception as e:
        print(f"Error: {e}")


# Фильтрация рулонов по нескольким диапазонам
@app.get("/multi_filter")
def multi_filter(id_down=None, id_up=None,
                 length_down=None, length_up=None,
                 weight_down=None, weight_up=None,
                 add_dt_down=None, add_dt_up=None,
                 del_dt_down=None, del_dt_up=None,
                 ):
    try:
        with Session(autoflush=False, bind=engine) as db:
            query = db.query(Rolls)
            if id_down is not None and id_up is not None:
                f = Rolls.weight.between(id_down, id_up)
                query = query.filter(f)
            if length_down is not None and length_up is not None:
                f = Rolls.weight.between(length_down, length_up)
                query = query.filter(f)
            if weight_down is not None and weight_up is not None:
                f = Rolls.weight.between(weight_down, weight_up)
                query = query.filter(f)
            if add_dt_down is not None and add_dt_up is not None:
                f = Rolls.add_dt.between(add_dt_down, add_dt_up)
                query = query.filter(f)
            if del_dt_down is not None and del_dt_up is not None:
                f = Rolls.del_dt.between(del_dt_down, del_dt_up)
                query = query.filter(f)
            rolls = query.all()
            rolls_data = []
            for roll in rolls:
                roll_data = {
                    "ID": roll.id,
                    "length": roll.length,
                    "weight": roll.weight,
                    "add_dt": roll.add_dt,
                    "del_dt": roll.del_dt
                }
                rolls_data.append(roll_data)
            return rolls_data
    except Exception as e:
        print(f"Error: {e}")


# Получение статистики по рулонам за определенный период
@app.get("/statistic")
def statistic(dt_down, dt_up):
    try:
        with Session(autoflush=False, bind=engine) as db:
            f = Rolls.add_dt.between(dt_down, dt_up)
            query = db.query(Rolls).filter(f)
            num_add_rolls = query.count()
            num_del_rolls = query.filter(Rolls.del_dt.isnot(None)).count()
            avg_length = round(db.query(func.avg(Rolls.length)).scalar(), 3)
            avg_weight = round(db.query(func.avg(Rolls.weight)).scalar(), 3)
            max_length = round(db.query(func.max(Rolls.length)).scalar(), 3)
            max_weight = round(db.query(func.max(Rolls.weight)).scalar(), 3)
            total_weight = round(db.query(func.sum(Rolls.weight)).scalar(), 3)
            max_duration = db.query(func.max(Rolls.del_dt - Rolls.add_dt))
            max_duration = max_duration.scalar()
            min_duration = db.query(func.min(Rolls.del_dt - Rolls.add_dt))
            min_duration = min_duration.scalar()
            data = {
                "Count added rolls": num_add_rolls,
                "Count deleted rolls": num_del_rolls,
                "Average length": avg_length,
                "Average weight": avg_weight,
                "Max length": max_length,
                "Max weight": max_weight,
                "Total weight": total_weight,
                "Max duration": max_duration,
                "Min duration": min_duration
            }
            return data
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
