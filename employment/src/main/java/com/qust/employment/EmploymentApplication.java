package com.qust.employment;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;

@MapperScan(basePackages = {"com.qust.employment.mapper"})
@SpringBootApplication(scanBasePackages = {"com.qust.employment"})
public class EmploymentApplication {

    public static void main(String[] args) {
        SpringApplication.run(EmploymentApplication.class, args);
    }

}
