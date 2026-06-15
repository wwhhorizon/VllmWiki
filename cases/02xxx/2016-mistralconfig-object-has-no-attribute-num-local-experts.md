# vllm-project/vllm#2016: 'MistralConfig' object has no attribute 'num_local_experts'

| 字段 | 值 |
| --- | --- |
| Issue | [#2016](https://github.com/vllm-project/vllm/issues/2016) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 'MistralConfig' object has no attribute 'num_local_experts'

### Issue 正文摘录

I have the Transformers from git and also installed vllm from git. I am trying to get the model up and running: https://huggingface.co/DiscoResearch/DiscoLM-mixtral-8x7b-v2 2023-12-11 10:12:18 | ERROR | stderr | File "/project/vllm_git/vllm/worker/model_runner.py", line 36, in load_model 2023-12-11 10:12:18 | ERROR | stderr | self.model = get_model(self.model_config) 2023-12-11 10:12:18 | ERROR | stderr | File "/project/vllm_git/vllm/model_executor/model_loader.py", line 117, in get_model 2023-12-11 10:12:18 | ERROR | stderr | model = model_class(model_config.hf_config, linear_method) 2023-12-11 10:12:18 | ERROR | stderr | File "/project/vllm_git/vllm/model_executor/models/mixtral.py", line 469, in __init__ 2023-12-11 10:12:18 | ERROR | stderr | self.layers = nn.ModuleList([ 2023-12-11 10:12:18 | ERROR | stderr | File "/project/vllm_git/vllm/model_executor/models/mixtral.py", line 470, in 2023-12-11 10:12:18 | ERROR | stderr | MixtralDecoderLayer(config) 2023-12-11 10:12:18 | ERROR | stderr | File "/project/vllm_git/vllm/model_executor/models/mixtral.py", line 416, in __init__ 2023-12-11 10:12:18 | ERROR | stderr | num_experts=config.num_local_experts, 2023-12-11 10:12:18 | ERROR...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 'MistralConfig' object has no attribute 'num_local_experts' I have the Transformers from git and also installed vllm from git. I am trying to get the model up and running: https://huggingface.co/DiscoResearch/DiscoLM-mi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: attribute 'num_local_experts' I have the Transformers from git and also installed vllm from git. I am trying to get the model up and running: https://huggingface.co/DiscoResearch/DiscoLM-mixtral-8x7b-v2 2023-12-11 10:12...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: trying to get the model up and running: https://huggingface.co/DiscoResearch/DiscoLM-mixtral-8x7b-v2 2023-12-11 10:12:18 | ERROR | stderr | File "/project/vllm_git/vllm/worker/model_runner.py", line 36, in load_model 20...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 'MistralConfig' object has no attribute 'num_local_experts' I have the Transformers from git and also installed vllm from git. I am trying to get the model up and running: https://huggingface.co/DiscoResearch/DiscoLM-mi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: al.py", line 470, in 2023-12-11 10:12:18 | ERROR | stderr | MixtralDecoderLayer(config) 2023-12-11 10:12:18 | ERROR | stderr | File "/project/vllm_git/vllm/model_executor/models/mixtral.py", line 416, in __init__ 2023-1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
