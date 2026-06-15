# vllm-project/vllm#20627: [Bug]: After wake_up sleeping model in OpenAI API server the model generate gibberish output

| 字段 | 值 |
| --- | --- |
| Issue | [#20627](https://github.com/vllm-project/vllm/issues/20627) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: After wake_up sleeping model in OpenAI API server the model generate gibberish output

### Issue 正文摘录

### Your current environment I am currentyly using v100 and I am loading 2 model (1 of them is qwen3 with gptq quantization and another gemma based model with bitsandbytes quantization) to GPU vllm=0.8.5.post1 version ### 🐛 Describe the bug I am currentyly using Tesla V100 and I am loading 2 model to GPU. Load one of them first put to sleep and load the other one. When I put one model into sleep mode and wake up the other, then put the other model back to sleep and wake up the other one, the models produces gibberish output. I am using sleep and wake_up methods from openai compatible api server dev mode enabled. Scenario: 1- Open vllm server at 8888 that runs qwen model 2- send sleep request to 8888 that runs qwen model 3- Open vllm server at 8889 that runs gemma model 4- send sleep request to 8889 that runs gemma model 5- send wake_up request to 8888 that runs qwen model 6- Perform inference with 8888 taht runs qwen model -> Non sense outputs 7- send sleep request to 8888 that runs qwen model 8- send wake_up request to 8889 that runs gemma model 9- Perform inference with 8889 that runs gemma model -> Non sense output

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: After wake_up sleeping model in OpenAI API server the model generate gibberish output bug;stale ### Your current environment I am currentyly using v100 and I am loading 2 model (1 of them is qwen3 with gptq quant...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eping model in OpenAI API server the model generate gibberish output bug;stale ### Your current environment I am currentyly using v100 and I am loading 2 model (1 of them is qwen3 with gptq quantization and another gemm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: emma based model with bitsandbytes quantization) to GPU vllm=0.8.5.post1 version ### 🐛 Describe the bug I am currentyly using Tesla V100 and I am loading 2 model to GPU. Load one of them first put to sleep and load the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: entyly using v100 and I am loading 2 model (1 of them is qwen3 with gptq quantization and another gemma based model with bitsandbytes quantization) to GPU vllm=0.8.5.post1 version ### 🐛 Describe the bug I am currentyly...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: m loading 2 model (1 of them is qwen3 with gptq quantization and another gemma based model with bitsandbytes quantization) to GPU vllm=0.8.5.post1 version ### 🐛 Describe the bug I am currentyly using Tesla V100 and I am...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
