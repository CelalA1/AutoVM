<?php use yii\widgets\ActiveForm;?>

<!-- content -->
<div class="content">     
    <div class="col-md-6">
        <?php echo \app\widgets\Alert::widget();?>
        <?php $form = ActiveForm::begin();?>
            <?php if($server->virtualization == 'KVM') {?>
            <?php echo $form->field($model, 'pool_name');?>
            <?php echo $form->field($model, 'pool_path');?>
            <?php } else {?>
            <?php echo $form->field($model, 'uuid');?>
            <?php echo $form->field($model, 'value');?>
            <?php }?>
            
            <?php echo $form->field($model, 'space');?>
            <div class="hide">
            <?php echo $form->field($model, 'is_default')->label('ISO files')->dropDownList(\app\models\Datastore::getDefaultYesNo());?>
            </div>
            <?php echo $form->field($model, 'vsan')->dropDownList(\app\models\Datastore::getVsanYesNo());?>
            <?php echo $form->field($model, 'is_public')->dropDownList(\app\models\Datastore::getPublicYesNo());?>
        
            <div class="margin-top-10"></div>
            <div class="margin-top-10"></div>
            
            <div class="form-group">
                <button type="submit" class="btn btn-primary waves-effect waves-light">Submit</button>
                <button type="reset" class="btn btn-danger">Reset</button>
            </div>
        <?php ActiveForm::end();?>
    </div>
</div>
<!-- END content -->
