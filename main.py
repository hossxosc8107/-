def get_lunar_date(year, month, day):
    # 1900年的正月初一对应的阳历日期
    start_date = datetime.date(1918, 5, 17)
    # 计算目标阳历日期距离1900年正月初一的天数
    offset = (datetime.date(year, month, day) - start_date).days
    # 天干名称
    heavenly_stems = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    # 地支名称
    earthly_branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    # 计算天干
    heavenly_stem = heavenly_stems[offset % 10] 
    # 计算地支
    earthly_branch = earthly_branches[offset % 12]
    # 返回天干地支
    return heavenly_stem + earthly_branch

lunar_date = get_lunar_date(2023, 4, 16)
print(lunar_date) 
