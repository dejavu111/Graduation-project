package com.qust.employment.mapper;

import com.qust.employment.po.DetailInfo;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;


@Mapper
@Repository
public interface DetailInfoMapper {


    int deleteByPrimaryKey(Integer id);

    int insert(DetailInfo record);

    int insertSelective(DetailInfo record);


    DetailInfo selectByPrimaryKey(Integer id);


    int updateByPrimaryKeySelective(DetailInfo record);

    int updateByPrimaryKey(DetailInfo record);

    DetailInfo selectByUUID(@Param("uuid") String uuid);
}