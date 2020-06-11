<?php

use yii\db\Migration;

/**
 * Class m200610_140209_update_datastore_columns
 */
class m200610_140209_update_datastore_columns extends Migration
{
    /**
     * {@inheritdoc}
     */
    public function safeUp()
    {
        $this->addColumn('datastore', 'pool_path', $this->string(255)->after('space'));
        $this->addColumn('datastore', 'pool_name', $this->string(255)->after('space'));
        
        $this->alterColumn('datastore', 'uuid', $this->string(255));
        $this->alterColumn('datastore', 'value', $this->string(255));   
    }

    /**
     * {@inheritdoc}
     */
    public function safeDown()
    {
        echo "m200610_140209_update_datastore_columns cannot be reverted.\n";

        return false;
    }

    /*
    // Use up()/down() to run migration code without a transaction.
    public function up()
    {

    }

    public function down()
    {
        echo "m200610_140209_update_datastore_columns cannot be reverted.\n";

        return false;
    }
    */
}
