# Terraform

[Terraform Without The Mess](https://speakerdeck.com/jen20/terraform-without-the-mess)

[An Introduction to Terraform](https://blog.gruntwork.io/an-introduction-to-terraform-f17df9c6d180#a9b0)

## Remote State

Me he centrado en AWS S3 + DynamoDB, he leído estos tres artículos (ordenados de mayor a menor detalle):

- [https://medium.com/faun/terraform-remote-backend-demystifiead-cb4132b95057](https://medium.com/faun/terraform-remote-backend-demystifiead-cb4132b95057) :exclamation: Este es el más completo y recuerda que hay que tener permisos restrictivos.
- [https://medium.com/@jessgreb01/how-to-terraform-locking-state-in-s3-2dc9a5665cb6](https://medium.com/@jessgreb01/how-to-terraform-locking-state-in-s3-2dc9a5665cb6)
- [https://www.techcrumble.net/2020/01/how-to-configure-terraform-aws-backend-with-s3-and-dynamodb-table/](https://www.techcrumble.net/2020/01/how-to-configure-terraform-aws-backend-with-s3-and-dynamodb-table/) :exclamation: Este está menos explicado pero el ejemplo me gusta más pues el setup lo tiene en terraform en lugar de en scripts tirando del AWS CLI.
- Aquí hay unos ejemplos y hay un directorio `s3-backend` donde hace el setup de s3 y dynamodb [https://github.com/gruntwork-io/intro-to-terraform](https://github.com/gruntwork-io/intro-to-terraform) via [https://blog.gruntwork.io/an-introduction-to-terraform-f17df9c6d180#a9b0](https://blog.gruntwork.io/an-introduction-to-terraform-f17df9c6d180#a9b0)
- Más detallado: [https://blog.gruntwork.io/how-to-manage-terraform-state-28f5697e68fa](https://blog.gruntwork.io/how-to-manage-terraform-state-28f5697e68fa)