package com.qust.employment.mapper;

import com.qust.employment.service.Impl.DetailInfoService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

/**
 * @author ：dejavu111
 * @date ：Created in 2019/4/1 15:51
 * @description：
 * @modified By：
 * @version: $
 */
@RunWith(SpringRunner.class)
@SpringBootTest
@AutoConfigureMockMvc
public class DetailInfoTest {



    @Autowired
    private DetailInfoService detailInfoService;

    @Test
    public void detailInfoTest(){
        System.out.println(detailInfoService.getDetailInfo(33));
    }
}
