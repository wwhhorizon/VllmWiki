# vllm-project/vllm#11484: [Bug]: xgrammar crashes with speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#11484](https://github.com/vllm-project/vllm/issues/11484) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: xgrammar crashes with speculative decoding

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I use xgrammer as guided decoding backend, it crashes with speculative decoding. It works well without speculative decoding. shell script: ```shell export VLLM_ATTENTION_BACKEND=FLASHINFER export TOKENIZERS_PARALLELISM=false model_path="./Qwen2-72B-Instruct-GPTQ-Int4/" speculative_model_path="./Qwen2-7B-Instruct-GPTQ-Int4/" max_model_len=8192 port=8000 max_num_seqs=32 max_num_batched_tokens=4096 python -m vllm.entrypoints.openai.api_server \ --model ${model_path} \ --served-model-name model \ --max-model-len ${max_model_len} \ --max-seq-len-to-capture ${max_model_len} \ --distributed-executor-backend mp \ --disable-log-requests \ --tensor-parallel-size 2 \ --pipeline-parallel-size 1 \ --disable-custom-all-reduce \ --uvicorn-log-level error \ --port ${port} \ --max-num-seqs ${max_num_seqs} \ --gpu-memory-utilization 0.95 \ --enable-prefix-caching \ --enable-chunked-prefill \ --max-num-batched-tokens ${max_num_batched_tokens} \ --speculative-model ${speculative_model_path} \ --speculative-draft-tensor-parallel-size 2 \ --num-speculative-tokens 3 \ --speculative-disable-by-batch-size 10 \ --c...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: xgrammar crashes with speculative decoding bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I use xgrammer as guided decoding backend, it cr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ecoding bug;structured-output;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I use xgrammer as guided decoding backend, it crashes with speculative decoding. It works...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: esponse_ ### 🐛 Describe the bug When I use xgrammer as guided decoding backend, it crashes with speculative decoding. It works well without speculative decoding. shell script: ```shell export VLLM_ATTENTION_BACKEND=FLAS...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: xport TOKENIZERS_PARALLELISM=false model_path="./Qwen2-72B-Instruct-GPTQ-Int4/" speculative_model_path="./Qwen2-7B-Instruct-GPTQ-Int4/" max_model_len=8192 port=8000 max_num_seqs=32 max_num_batched_tokens=4096 python -m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
