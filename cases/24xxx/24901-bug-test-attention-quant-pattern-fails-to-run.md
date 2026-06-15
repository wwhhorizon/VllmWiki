# vllm-project/vllm#24901: [Bug]: test_attention_quant_pattern fails to run

| 字段 | 值 |
| --- | --- |
| Issue | [#24901](https://github.com/vllm-project/vllm/issues/24901) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: test_attention_quant_pattern fails to run

### Issue 正文摘录

### Your current environment `pytest tests/compile/test_fusion_attn.py -k test_attention_quant_pattern` errors with `Segmentation fault` on B200. ### 🐛 Describe the bug `pytest tests/compile/test_fusion_attn.py -k test_attention_quant_pattern` errors with `Segmentation fault`. I have installed flash infer. On the same machine and conda environment, I can run successfully `vllm bench latency --model nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --tensor-parallel-size 8 --trust-remote-code -O.pass_config.enable_attn_fusion=true -O.pass_config.enable_noop=true -O.custom_ops+=+quant_fp8 --kv-cache-dtype=fp8 -O.splitting_ops=[] -O.cudagraph_mode=PIECEWISE -O.use_inductor_graph_partition=true`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ant_pattern fails to run bug ### Your current environment `pytest tests/compile/test_fusion_attn.py -k test_attention_quant_pattern` errors with `Segmentation fault` on B200. ### 🐛 Describe the bug `pytest tests/compile...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: test_attention_quant_pattern fails to run bug ### Your current environment `pytest tests/compile/test_fusion_attn.py -k test_attention_quant_pattern` errors with `Segmentation fault` on B200. ### 🐛 Describe the b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: .py -k test_attention_quant_pattern` errors with `Segmentation fault` on B200. ### 🐛 Describe the bug `pytest tests/compile/test_fusion_attn.py -k test_attention_quant_pattern` errors with `Segmentation fault`. I have i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: hine and conda environment, I can run successfully `vllm bench latency --model nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 --tensor-parallel-size 8 --trust-remote-code -O.pass_config.enable_attn_fusion=true -O.pass_config...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: test_attention_quant_pattern fails to run bug ### Your current environment `pytest tests/compile/test_fusion_attn.py -k test_attention_quant_pattern` errors with `Segmentation fault` on B200. ### 🐛 Describe the b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
