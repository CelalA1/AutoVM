<?php
use yii\helpers\Url;
use yii\widgets\ActiveForm;
?>

<style>
    .nav-tabs{
        margin-bottom:20px;    
    }
    
    .nav-tabs li{
        border-bottom:1px solid #ddd;   
    }
    
    .mts{
        margin:10px 0;
    }
    
    .hide{
        display:none;   
    }
</style>

<div class="content">
    <div class="col-md-6">
        <ul class="nav nav-tabs">
            <li class="active"><a href="#one" data-toggle="tab">VMWare ESXi</a></li>
            <li><a href="#two" data-toggle="tab">KVM</a></li>
        </ul>
                    
        <?php echo \app\widgets\Alert::widget();?>
            
        <div class="tab-content">
            <div class="tab-pane active" id="one">
                <?php $form = ActiveForm::begin();?>

                <?php echo $form->field($model, 'name');?>
                <?php echo $form->field($model, 'ip');?>
                <?php echo $form->field($model, 'port')->textInput(['value' => '22']);?>
                <?php echo $form->field($model, 'username');?>
                <?php echo $form->field($model, 'password')->passwordInput();?>
                <?php echo $form->field($model, 'network')->label('VM Network Label')->textInput(['value' => 'VM Network']);?>
                <?php echo $form->field($model, 'second_network')->label('Second Network Label');?>
                <?php echo $form->field($model, 'version')->label('VM Hardware version')->dropDownList(\app\models\Server::getVersionList());?>
                <?php echo $form->field($model, 'vcenter_ip');?>
                <?php echo $form->field($model, 'vcenter_username');?>
                <?php echo $form->field($model, 'vcenter_password')->passwordInput();?>
                <?php echo $form->field($model, 'parent_id')->label('Use IP Address from:')->dropDownList(\app\models\Server::getListData(), ['prompt' => 'None']);?>
                <?php echo $form->field($model, 'virtualization')->dropDownList(\app\models\Server::getVirtualizationList());?>

                <?php echo $form->field($model, 'dns1')->textInput(['value' => '4.2.2.4']);?>
                <?php echo $form->field($model, 'dns2')->textInput(['value' => '8.8.8.8']);?>

                <div class="hide">
                <?php echo $form->field($model, 'server_address')->textInput(['value' => Url::toRoute('/candy/default', true) ]);?>
                </div>

                <div class="mts"></div>

                <div class="form-group">
                    <button type="submit" class="btn btn-primary waves-effect waves-light">Submit</button>
                    <button type="reset" class="btn btn-danger">Reset</button>
                </div>

                <?php ActiveForm::end();?>
            </div>
            
            <div class="tab-pane" id="two">
                <?php $form = ActiveForm::begin();?>

                <?php echo $form->field($model, 'name');?>
                <?php echo $form->field($model, 'ip');?>
                <?php echo $form->field($model, 'port')->textInput(['value' => '22']);?>
                <?php echo $form->field($model, 'username');?>
                <?php echo $form->field($model, 'password')->passwordInput();?>
                
                <div class="hide">
                <?php echo $form->field($model, 'network')->label('VM Network Label')->textInput(['value' => 'VM Network']);?>
                <?php echo $form->field($model, 'second_network')->label('Second Network Label');?>
                <?php echo $form->field($model, 'version')->label('VM Hardware version')->dropDownList(\app\models\Server::getVersionList());?>
                <?php echo $form->field($model, 'vcenter_ip');?>
                <?php echo $form->field($model, 'vcenter_username');?>
                <?php echo $form->field($model, 'vcenter_password')->passwordInput();?>
                </div>
                
                <?php echo $form->field($model, 'parent_id')->label('Use IP Address from:')->dropDownList(\app\models\Server::getListData(), ['prompt' => 'None']);?>
                <?php echo $form->field($model, 'virtualization')->dropDownList(\app\models\Server::getVirtualizationList());?>

                <?php echo $form->field($model, 'dns1')->textInput(['value' => '4.2.2.4']);?>
                <?php echo $form->field($model, 'dns2')->textInput(['value' => '8.8.8.8']);?>
                
                <?php echo $form->field($model, 'rsa')->textArea();?>

                <div class="hide">
                <?php echo $form->field($model, 'server_address')->textInput(['value' => Url::toRoute('/kvm/default', true) ]);?>
                </div>

                <div class="mts"></div>

                <div class="form-group">
                    <button type="submit" class="btn btn-primary waves-effect waves-light">Submit</button>
                    <button type="reset" class="btn btn-danger">Reset</button>
                </div>

                <?php ActiveForm::end();?>
            </div>
        </div>
    </div>
</div>