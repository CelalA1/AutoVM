<?php

namespace app\models;

use Yii;
use yii\behaviors\TimestampBehavior;

/**
 * This is the model class for table "os".
 *
 * @property string $id
 * @property string $name
 * @property string $type
 * @property string $operation_system
 * @property string $username
 * @property string $password
 * @property string $adapter
 * @property string $created_at
 * @property string $updated_at
 *
 * @property Vps[] $vps
 */
class Os extends \yii\db\ActiveRecord
{
    const STATUS_ACTIVE = 1;
    const STATUS_INACTIVE = 2;

    /**
     * @inheritdoc
     */
    public static function tableName()
    {
        return 'os';
    }

    /**
     * @inheritdoc
     */
    public function rules()
    {
        return [
            [['name', 'type', 'kvm_type', 'operation_system', 'guest', 'username', 'password', 'adapter'], 'required'],
            [['created_at', 'updated_at', 'status'], 'integer'],
            [['name', 'type', 'kvm_type', 'operation_system', 'guest', 'username', 'password', 'adapter'], 'string', 'max' => 255],
        ];
    }

    /**
     * @inheritdoc
     */
    public function attributeLabels()
    {
        return [
            'id' => Yii::t('app', 'ID'),
            'name' => Yii::t('app', 'Name'),
            'type' => Yii::t('app', 'Type'),
            'kvm_type' => Yii::t('app', 'KVM Type'),
			'username' => Yii::t('app', 'Username'),
			'password' => Yii::t('app', 'Password'),
            'adapter' => Yii::t('app', 'Adapter'),
            'guest' => Yii::t('app', 'Guest'),
            'created_at' => Yii::t('app', 'Created At'),
            'updated_at' => Yii::t('app', 'Updated At'),
            'status' => Yii::t('app', 'Status'),
            'operation_system' => Yii::t('app', 'Operating System'),

        ];
    }
   

    /**
     * @return \yii\db\ActiveQuery
     */
    public function getVps()
    {
        return $this->hasMany(Vps::className(), ['os_id' => 'id']);
    }

    /**
     * @inheritdoc
     * @return \app\models\queries\OsQuery the active query used by this AR class.
     */
    public static function find()
    {
        return new \app\models\queries\OsQuery(get_called_class());
    }

    public static function getOperationSystem()
    {
     	$list =  array(
                'windows 2012 64 bit',
                'windows 2016 64 bit',
                'windows 2019 64 bit',
                'windows 8 32 bit',
                'windows 8 64 bit',
                'ubuntu 16.04 32 bit',
                'ubuntu 16.04 64 bit',
                'ubuntu 18.04 32 bit',
                'ubuntu 18.04 64 bit',
                'centos 7 64 bit',  
                'centos 8 64 bit',  
                'debian 10 32 bit',
                'debian 10 64 bit',
            );

	    return array_combine($list, $list);
    }
    
    public static function getAdapters()
    {
        return [
            'e1000' => 'e1000',  
            'e1000e' => 'e1000e',
            'vmxnet3' => 'vmxnet3',           
        ];
    }
    
    public static function getGuests()
    {
        return [
            'windows8srv-64' => 'Windows 2012 64 bit',
            'windows9srv-64' => 'Windows 2016 or later 64 bit',
            'windows8' => 'Windows 8 32 bit',
            'windows8-64' => 'Windows 8 64 bit',
            'ubuntu' => 'Ubuntu 32 bit',
            'ubuntu-64' => 'Ubuntu 64 bit',
            'centos' => 'CentOS 32 bit',
            'centos-64' => 'CentOS 64 bit',
            'centos7-64' => 'CentOS 7 64 bit',
            'centos8-64' => 'CentOS 8 64 bit',
            'debian8' => 'Debian 8 32 bit',
            'debian8-64' => 'Debian 8 64 bit',
            'debian9' => 'Debian 9 32 bit',
            'debian9-64' => 'Debian 9 64 bit',
            'debian10' => 'Debian 10 32 bit',
            'debian10-64' => 'Debian 10 64 bit',
        ];
    }

    public static function getStatusList()
    {
        return [
            self::STATUS_ACTIVE => Yii::t('app', 'Active'),
            self::STATUS_INACTIVE => Yii::t('app', 'Inactive'),
        ];
    }
    
    public function scenarios()
    {
        return [
            self::SCENARIO_DEFAULT => ['name', 'type', 'kvm_type', 'username', 'password', 'adapter', 'guest', 'status'],
        ];
    }
        
    public function behaviors()
    {
        return [
            TimestampBehavior::className(),
        ];
    }
}
 
