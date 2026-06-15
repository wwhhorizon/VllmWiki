# vllm-project/vllm#13085: [Feature]: About supporting the deepseek-r1 gguf model.

| 字段 | 值 |
| --- | --- |
| Issue | [#13085](https://github.com/vllm-project/vllm/issues/13085) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: About supporting the deepseek-r1 gguf model.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch "Could you please confirm if version 0.7.2 supports the r1-gguf format? I encountered the following issue upon launch." WARNING 02-11 18:13:02 config.py:993] MLA is not supported with gguf quantization. Disabling MLA. WARNING 02-11 18:13:10 config.py:993] MLA is not supported with gguf quantization. Disabling MLA. WARNING 02-11 18:13:10 config.py:993] MLA is not supported with gguf quantization. Disabling MLA. WARNING 02-11 18:13:10 config.py:993] MLA is not supported with gguf quantization. Disabling MLA. ERROR 02-11 18:13:11 engine.py:389] Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 380, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 123, in from_engine_args return cls(ipc_path=ipc_path, ^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 75, in __init__ self.engine = LLMEngine(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^ Fi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: About supporting the deepseek-r1 gguf model. feature request ### 🚀 The feature, motivation and pitch "Could you please confirm if version 0.7.2 supports the r1-gguf format? I encountered the following issue u...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: r/models/deepseek_v2.py", line 528, in __init__ self.mlp = DeepseekV2MoE( ^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/deepseek_v2.py", line 129, in __init__ self.experts = Fus...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: About supporting the deepseek-r1 gguf model. feature request ### 🚀 The feature, motivation and pitch "Could you please confirm if version 0.7.2 supports the r1-gguf format? I encountered the following issue u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: st ### 🚀 The feature, motivation and pitch "Could you please confirm if version 0.7.2 supports the r1-gguf format? I encountered the following issue upon launch." WARNING 02-11 18:13:02 config.py:993] MLA is not support...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ." WARNING 02-11 18:13:02 config.py:993] MLA is not supported with gguf quantization. Disabling MLA. WARNING 02-11 18:13:10 config.py:993] MLA is not supported with gguf quantization. Disabling MLA. WARNING 02-11 18:13:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
