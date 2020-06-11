<?php

use yii\db\Migration;

/**
 * Class m200610_135803_add_kvm_type_column
 */
class m200610_135803_add_kvm_type_column extends Migration
{
    /**
     * {@inheritdoc}
     */
    public function safeUp()
    {
        $this->addColumn('os', 'kvm_type', $this->string(255)->after('type'));
    }

    /**
     * {@inheritdoc}
     */
    public function safeDown()
    {
        echo "m200610_135803_add_kvm_type_column cannot be reverted.\n";

        return false;
    }

    /*
    // Use up()/down() to run migration code without a transaction.
    public function up()
    {

    }

    public function down()
    {
        echo "m200610_135803_add_kvm_type_column cannot be reverted.\n";

        return false;
    }
    */
}
