# vllm-project/vllm#24714: [Bug]: Hunyuan-7B-Instruct get error output

| 字段 | 值 |
| --- | --- |
| Issue | [#24714](https://github.com/vllm-project/vllm/issues/24714) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hunyuan-7B-Instruct get error output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Vllm-serving running Hunyuan-7B-Instruct will get error output. image: vllm/vllm-openai:latest or vllm/vllm-openai:0.10.0 serving bash ```bash my_model="Hunyuan-7B-Instruct" #my_model="Hunyuan-7B-Instruct-0124" export model="/llm/models/models/"$my_model export served_model_name=$my_model export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 export VLLM_OFFLOAD_WEIGHTS_BEFORE_QUANT=1 CUDA_VISIBLE_DEVICES=1 echo $model export VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server \ --model $model \ --served-model-name $served_model_name \ --port 8001 \ --trust-remote-code \ --gpu-memory-utilization 0.90 \ --enforce-eager \ --dtype float16 \ --max-model-len 3000 \ --distributed-executor-backend ray \ --max-num-batched-tokens 3000 \ --max-num-seqs 32 \ --tensor-parallel-size 1 \ --block-size 64 \ --pipeline-parallel-size "1" ``` error.log ```bash curl http://localhost:8001/v1/completions -H "Content-Type: application/json" -d '{ "model": "Hunyuan-7B-Instruct", "prompt": "What is AI?", "max_tokens": 41 }' {"id":"cmpl-b994b194c3104b6d95ca43c0e10819e3","object":"text_completion","created":1757641646,"model":"Hunyuan-7B-Instruct","choices":[{"ind...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: xport VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 export VLLM_OFFLOAD_WEIGHTS_BEFORE_QUANT=1 CUDA_VISIBLE_DEVICES=1 echo $model export VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server \ --model $model \ --served-model-na...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: \ --dtype float16 \ --max-model-len 3000 \ --distributed-executor-backend ray \ --max-num-batched-tokens 3000 \ --max-num-seqs 32 \ --tensor-parallel-size 1 \ --block-size 64 \ --pipeline-parallel-size "1" ``` error.log...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: M_ALLOW_LONG_MAX_MODEL_LEN=1 export VLLM_OFFLOAD_WEIGHTS_BEFORE_QUANT=1 CUDA_VISIBLE_DEVICES=1 echo $model export VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server \ --model $model \ --served-model-name $serve...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: hed-tokens 3000 \ --max-num-seqs 32 \ --tensor-parallel-size 1 \ --block-size 64 \ --pipeline-parallel-size "1" ``` error.log ```bash curl http://localhost:8001/v1/completions -H "Content-Type: application/json" -d '{ "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
