# vllm-project/vllm#2404: The first word return of 4bit awq model is very slow

| 字段 | 值 |
| --- | --- |
| Issue | [#2404](https://github.com/vllm-project/vllm/issues/2404) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> The first word return of 4bit awq model is very slow

### Issue 正文摘录

I used vllm to deploy the awq-quantized 4-bit Yi-34B model on A100 80G, the test results show that in the case of long prompt, the 4bit model takes a long time to return the first word result, much longer than the 16bit model. However, after the first word result is returned, the output speed of the 4-bit model is faster than that of the 16-bit model. Why is this? The following are the specific test results: model | bits | device | input length | output length | first token takes time/second | Complete request takes time/second -- | -- | -- | -- | -- | -- | -- Yi-34B | 16bit | A100-80G*1 | 2649 | 172 | 1.0577 | 9.2391 Yi-34B | awq-4bit | A100-80G*1 | 2649 | 170 | 3.295 | 8.142

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ter than that of the 16-bit model. Why is this? The following are the specific test results: model | bits | device | input length | output length | first token takes time/second | Complete request takes time/second -- |...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: word return of 4bit awq model is very slow I used vllm to deploy the awq-quantized 4-bit Yi-34B model on A100 80G, the test results show that in the case of long prompt, the 4bit model takes a long time to return the fi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: very slow I used vllm to deploy the awq-quantized 4-bit Yi-34B model on A100 80G, the test results show that in the case of long prompt, the 4bit model takes a long time to return the first word result, much longer than...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: The first word return of 4bit awq model is very slow I used vllm to deploy the awq-quantized 4-bit Yi-34B model on A100 80G, the test results show that in the case of long prompt, the 4bit model takes a long time to ret...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: input length | output length | first token takes time/second | Complete request takes time/second -- | -- | -- | -- | -- | -- | -- Yi-34B | 16bit | A100-80G*1 | 2649 | 172 | 1.0577 | 9.2391 Yi-34B | awq-4bit | A100-80G*...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
