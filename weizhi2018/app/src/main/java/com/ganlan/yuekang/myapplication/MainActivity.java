package com.ganlan.yuekang.myapplication;

import android.content.SharedPreferences;
import android.hardware.SensorManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.text.TextUtils;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;


public abstract class MainActivity extends AppCompatActivity {

    private String menuStr;
    private int menuResId;
    private String menuStr2;
    private int menuResId2;
    private TextView tvTitle;
    private FrameLayout viewContent;
    private Toolbar toolbar;

    private EditText et01;
    private Button bt01;

    private SharedPreferences sp;

    MyOnClickListener listener = new MyOnClickListener();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initView();
        sp = getSharedPreferences("configs",MODE_PRIVATE);

        //1、设置支出，并不显示项目的title文字
        toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        getSupportActionBar().setDisplayShowTitleEnabled(false);

        //2、将子类的布局解析到 FrameLayout 里面
        viewContent = (FrameLayout) findViewById(R.id.viewContent);
        LayoutInflater.from(this).inflate(getConentView(), viewContent);

        //3、初始化操作（此方法必须放在最后执行位置）
        init(savedInstanceState);
    }

    private void initView() {

        et01 =  (EditText)findViewById(R.id.et01);
        bt01 = (Button) findViewById(R.id.bt01);

        bt01.setOnClickListener(listener);
    }
    /**
     * 设置布局资源
     *
     * @return
     */
    protected abstract int getConentView();
    /**
     * 初始化操作
     *
     * @param savedInstanceState
     */
    protected abstract void init(Bundle savedInstanceState);

    class MyOnClickListener implements View.OnClickListener{
        @Override
        public void onClick(View v) {
            switch (v.getId()){
                case R.id.bt01:
                    String juli = et01.getText().toString().trim();
                    if (TextUtils.isEmpty(juli)){
                        return;
                    }
                    if (isNumeric(juli)){


                        SharedPreferences.Editor editor = sp.edit();
                        //  存储数据
                        editor.putString("juli",juli);
                        boolean commit = editor.commit();
                        if (commit){
                            Toast.makeText(MainActivity.this,"保存成功！设置距离为："+juli+"米。",Toast.LENGTH_SHORT).show();
                        }
                        break;
                    }
                    else{
                        Toast.makeText(MainActivity.this,"请输入整数距离！！",Toast.LENGTH_LONG).show();
                    }
            }
        }

        boolean isNumeric(String s) {
            if (s != null && !"".equals(s.trim()))
                return s.matches("^[0-9]*$");
            else
                return false;
        }
    }
    /**
     * 设置显示返回按钮
     */
    protected void setTitleBack(boolean visible) {
        if (visible) {
            toolbar.setNavigationIcon(R.mipmap.back_whait);//设置返回按钮
        }
    }


}
