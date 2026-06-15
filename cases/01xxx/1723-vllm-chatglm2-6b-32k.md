# vllm-project/vllm#1723: vllm加载ChatGLM2-6B-32K报错

| 字段 | 值 |
| --- | --- |
| Issue | [#1723](https://github.com/vllm-project/vllm/issues/1723) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vllm加载ChatGLM2-6B-32K报错

### Issue 正文摘录

通过Python环境加载vllm0.2.2，加载ChatGLM2-6B-32K模型，发现报出如下NCCL相关问题。报错信息如下： >>> llm = LLM(model="/home/cloud/LLM/THUDM/chatglm2-6b-32k", trust_remote_code=True) INFO 11-20 16:58:30 llm_engine.py:72] Initializing an LLM engine with config: model='/home/cloud/LLM/THUDM/chatglm2-6b-32k', tokenizer='/home/cloud/LLM/THUDM/chatglm2-6b-32k', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) WARNING 11-20 16:58:30 tokenizer.py:66] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. Traceback (most recent call last): File " ", line 1, in File "/home/cloud/anaconda3/envs/vllm_awq/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 93, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/home/cloud/anaconda3/envs/vllm_awq/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 231, in from_engine_args engine = cls(*engine_configs, File "/home/cloud/anaconda3/envs/vllm_awq/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 110, in __init__ se...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) WARNING 11-20 16:5...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: on环境加载vllm0.2.2，加载ChatGLM2-6B-32K模型，发现报出如下NCCL相关问题。报错信息如下： >>> llm = LLM(model="/home/cloud/LLM/THUDM/chatglm2-6b-32k", trust_remote_code=True) INFO 11-20 16:58:30 llm_engine.py:72] Initializing an LLM engine with confi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:219, invalid argument, NCCL version 2.14.3 ncclInvalidArgument: Invalid value for an argument. Last error: Invalid config blocking attribute value -2147483648 performance dis...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _reduce work = group.allreduce([tensor], opts) torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:219, invalid argument, NCCL version 2.14.3 ncclInvalidArgument: Invalid valu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _distributed_environment torch.distributed.all_reduce(torch.zeros(1).cuda()) File "/home/cloud/anaconda3/envs/vllm_awq/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 47, in wrapper return func(*arg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
