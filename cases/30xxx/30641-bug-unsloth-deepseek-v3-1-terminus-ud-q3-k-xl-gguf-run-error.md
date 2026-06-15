# vllm-project/vllm#30641: [Bug]: unsloth DeepSeek-V3.1-Terminus-UD-Q3_K_XL gguf run error

| 字段 | 值 |
| --- | --- |
| Issue | [#30641](https://github.com/vllm-project/vllm/issues/30641) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: unsloth DeepSeek-V3.1-Terminus-UD-Q3_K_XL gguf run error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug my env: 8*H800-PCIe model: unsloth DeepSeek-V3.1-Terminus-UD-Q3_K_XL.gguf vllm: v0.11.0 my command: python3 -m vllm.entrypoints.openai.api_server --model /models/UD-Q3_K_XL/DeepSeek-V3.1-Terminus-UD-Q3_K_XL.gguf --seed 3407 --served-model-name "deepseekv3" --enable-chunked-prefill --max-num-batched-tokens 4096 --hf-config-path /models/UD-Q3_K_XL/ --tokenizer /models/UD-Q3_K_XL/ --gpu-memory-utilization 0.9 --max-model-len 16384 --trust-remote-code --tensor-parallel-size 8 --host 0.0.0.0 --port 9100 I follow this issue, https://github.com/vllm-project/vllm/pull/13167, and run unsloth DeepSeek-V3-0324 q2_k sucessfully，However, an error occurred when launching the DeepSeek-V3.1-Terminus-UD-Q3_K_XL.gguf model. So I switched to vllm-v0.11.0, but the problem persisted. root@node51:/vllm-workspace# python3 -m vllm.entrypoints.openai.api_server \ --model /workspace/v3.1-Terminus/DeepSeek-V3.1-Terminus-UD-Q3_K_XL.gguf \ --seed 3407 --served-model-name "deepseek-v3" \ --enable-chunked-prefill --max-num-batched-tokens 512 \ --hf-config-path /workspace/v3.1-Terminus/ \ --tokenizer /workspace/v3.1-Terminus/ \ --gpu-memory-utilization 0.9 --ma...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Your current environment ### 🐛 Describe the bug my env: 8*H800-PCIe model: unsloth DeepSeek-V3.1-Terminus-UD-Q3_K_XL.gguf vllm: v0.11.0 my command: python3 -m vllm.entrypoints.openai.api_server --model /models/UD-Q3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 1:21:41 [multiproc_executor.py:597] self.model_runner.load_model(eep_scale_up=eep_scale_up) (Worker_TP2 pid=11851) ERROR 12-13 21:21:41 [multiproc_executor.py:597] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Your current environment ### 🐛 Describe the bug my env: 8*H800-PCIe model: unsloth DeepSeek-V3.1-Terminus-UD-Q3_K_XL.gguf vllm: v0.11.0 my command: python3 -m vllm.entrypoints.openai.api_server --model /models/UD-Q3_K_X...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: unsloth DeepSeek-V3.1-Terminus-UD-Q3_K_XL gguf run error bug;stale ### Your current environment ### 🐛 Describe the bug my env: 8*H800-PCIe model: unsloth DeepSeek-V3.1-Terminus-UD-Q3_K_XL.gguf vllm: v0.11.0 my co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: y:597] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attention/backends/mla/common.py", line 1329, in process_weights_after_loading (Worker_TP2 pid=11851) ERROR 12-13 21:21:41 [multiproc_executor.py:597] kv_b_pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
