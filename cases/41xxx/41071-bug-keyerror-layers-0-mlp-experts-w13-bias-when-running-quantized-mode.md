# vllm-project/vllm#41071: [Bug]: KeyError: 'layers.0.mlp.experts.w13_bias' when running quantized model on vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#41071](https://github.com/vllm-project/vllm/issues/41071) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'layers.0.mlp.experts.w13_bias' when running quantized model on vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm getting the following error when trying to serve a quantized model through vLLM. Tried v0.18 and v0.19 Tried: TevunahAi/gpt-oss-120b-1024-Calibration-FP8 unsloth/gpt-oss-120b-unsloth-bnb-4bit and a model I quantized using llm-compressor all presented the same behavior. For TevunahAi I tried running it with just these params: ``` vllm serve TevunahAi/gpt-oss-120b-1024-Calibration-FP8 --dtype auto --max-model-len 8192 ``` All the cases showed the same error. Am I doing something wrong? ``` Loading safetensors checkpoint shards: 1% Completed | 1/73 [00:20<25:09, 20.96s/it] (Worker_TP0 pid=624) (Worker_TP0 pid=624) ERROR 04-19 16:21:20 [multiproc_executor.py:857] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/gpt_oss.py", line 1225, in load_weights (Worker_TP0 pid=624) ERROR 04-19 16:21:20 [multiproc_executor.py:857] return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper) (Worker_TP0 pid=624) ERROR 04-19 16:21:20 [multiproc_executor.py:857] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=624) ERROR 04-19 16:21:20 [multiproc_executor.py:857] File "/usr/local/lib/pyth...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: KeyError: 'layers.0.mlp.experts.w13_bias' when running quantized model on vLLM bug ### Your current environment ### 🐛 Describe the bug I'm getting the following error when trying to serve a quantized model throug...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: KeyError: 'layers.0.mlp.experts.w13_bias' when running quantized model on vLLM bug ### Your current environment ### 🐛 Describe the bug I'm getting the following error when trying to serve a quantized model throug...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: KeyError: 'layers.0.mlp.experts.w13_bias' when running quantized model on vLLM bug ### Your current environment ### 🐛 Describe the bug I'm getting the following error when trying to serve a quantized model throug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
