package com.qust.employment.mapper;

import com.qust.employment.po.ListInfo;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

import java.util.Date;
import java.util.List;
import java.util.Map;

@Mapper
@Repository
public interface ListInfoMapper {

    int deleteByPrimaryKey(Integer id);

    int insert(ListInfo record);

    int insertSelective(ListInfo record);

    ListInfo selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(ListInfo record);

    int updateByPrimaryKey(ListInfo record);

    List<ListInfo> selectAll(@Param("currentDate") Date currentDate, @Param("pageNum") int pageNum, @Param("pageSize") int pageSize);

    List<Map<String, Object>>  selectAlltotalpages(@Param("currentDate") Date currentDate);
}