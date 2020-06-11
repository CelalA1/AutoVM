<?php

namespace app\modules\kvm\controllers;

use Yii;
use yii\web\Controller;

class DefaultController extends Controller
{
    public $enableCsrfValidation = false;
    
    public function behaviors()
    {
        return ['app\filters\Format'];
    }
    
    public function actionInstall()
    {
        return $this->python('install.py', true);   
    }
    
    public function actionStatus()
    {
        return $this->python('status.py');   
    }
    
    public function actionStep()
    {
        return $this->python('step.py');   
    }
    
    public function actionStart()
    {
        return $this->python('start.py');   
    }
    
    public function actionStop()
    {
        return $this->python('stop.py');   
    }
    
    public function actionReboot()
    {
        return $this->python('reboot.py');   
    }
    
    public function actionSuspend()
    {
        return $this->python('suspend.py');   
    }
    
    public function actionUsage()
    {
        return $this->python('usage.py');   
    }
    
    public function actionAllStatus()
    {
        return $this->python('all_status.py');
    }
    
    public function actionBandwidth()
    {
        return $this->python('bandwidth.py');   
    }
    
    public function actionConsole()
    {
        return $this->python('console.py');   
    }
    
    protected function python($python, $background = false)
    {
        $python = Yii::getAlias("@app/modules/kvm/python/$python");
        
        $params = http_build_query($_POST);
        
        if ($background) {
            $command = ['nohup', 'python2.7'];   
        } else {
            $command = ['python2.7'];   
        }
        
        $append = [$python, $params];
        
        if ($background) {
            $append[] = '&';  
        }
        
        $command = escapeshellcmd(implode(' ', array_merge($command, $append)));
        
        # Execute command
        $result = shell_exec($command);
        
        if (empty($result)) {
            return ['ok' => false];   
        }
        
        return json_decode($result);
    }
}