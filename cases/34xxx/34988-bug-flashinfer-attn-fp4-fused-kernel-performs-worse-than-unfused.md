# vllm-project/vllm#34988: [Bug]: FlashInfer attn-fp4 fused kernel performs worse than unfused

| 字段 | 值 |
| --- | --- |
| Issue | [#34988](https://github.com/vllm-project/vllm/issues/34988) |
| 状态 | open |
| 标签 | bug;performance;torch.compile;needs reproduction;nvidia |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | kernel;quantization |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer attn-fp4 fused kernel performs worse than unfused

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Benchmarking sweeps for a few models. Base command: ``` # base command vllm bench sweep serve \ --serve-cmd "vllm serve --model $MODEL --tensor-parallel-size $TP --port $PORT --no-enable-prefix-caching" \ --bench-cmd "vllm bench serve --dataset-name random --ignore-eos --model=$MODEL --port $PORT" \ --bench-params sweep-qps.json \ --serve-params sweep-attn-quant.json \ # sweep-qps.json [ { "num-prompts": 120, "request-rate": 1 },{ "num-prompts": 600, "request-rate": 5 },{ "num-prompts": 1200, "request-rate": 10 },{ "num-prompts": 1800, "request-rate": 15 },{ "num-prompts": 2400, "request-rate": 20 },{ "num-prompts": 1000, "request-rate": "inf" } ] # sweep-attn-quant.json { "fused-attn-quant": { "compilation_config": { "use_inductor_graph_partition": true, "pass_config": { "fuse_attn_quant": true } } }, "unfused-attn-quant": { "compilation_config": { "use_inductor_graph_partition": true, "pass_config": { "fuse_attn_quant": false } } } } ``` ## Models ### `nvidia/Llama-3.1-8B-Instruct-NVFP4 tp=1` ### `nvidia/Llama-3.3-70B-Instruct-NVFP4 tp=4` ### `nvidia/Qwen3-30B-A3B-NVFP4 tp=1` ### Before submitting a new issue... - [x] Make sure...

## 现有链接修复摘要

#36083 Add adaptive decode chunking for SM100 fused TRTLLM path (TMP FIX)#34988

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: attn-fp4 fused kernel performs worse than unfused bug;performance;torch.compile;needs reproduction;nvidia ### Your current environment ### 🐛 Describe the bug Benchmarking sweeps for a few models. Base command: ``` # bas...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nt environment ### 🐛 Describe the bug Benchmarking sweeps for a few models. Base command: ``` # base command vllm bench sweep serve \ --serve-cmd "vllm serve --model $MODEL --tensor-parallel-size $TP --port $PORT --no-e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FlashInfer attn-fp4 fused kernel performs worse than unfused bug;performance;torch.compile;needs reproduction;nvidia ### Your current environment ### 🐛 Describe the bug Benchmarking sweeps for a few models. Base...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: p-attn-quant.json \ # sweep-qps.json [ { "num-prompts": 120, "request-rate": 1 },{ "num-prompts": 600, "request-rate": 5 },{ "num-prompts": 1200, "request-rate": 10 },{ "num-prompts": 1800, "request-rate": 15 },{ "num-p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36083](https://github.com/vllm-project/vllm/pull/36083) | closes_keyword | 0.95 |  Add adaptive decode chunking for SM100 fused TRTLLM path (TMP FIX)#34988 | FIX)#34988 ## Purpose find top kernel:https://paste.ubuntu.com/p/G4FytRwYnP/ res: https://paste.ubuntu.com/p/7MHTBdKYbB/ Add a temporary backend-side mitigation for SM100 decode |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
