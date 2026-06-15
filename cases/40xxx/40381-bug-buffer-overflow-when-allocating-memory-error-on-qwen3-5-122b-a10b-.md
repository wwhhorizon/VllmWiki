# vllm-project/vllm#40381: [Bug]: Buffer overflow when allocating memory error on Qwen3.5-122B-A10B-GPTQ-Int4 and NVFP4

| 字段 | 值 |
| --- | --- |
| Issue | [#40381](https://github.com/vllm-project/vllm/issues/40381) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Buffer overflow when allocating memory error on Qwen3.5-122B-A10B-GPTQ-Int4 and NVFP4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The bug can be safely reproduce on Spark, B100 and B200(single GPU device) on latest build(v0.19.1) pull the image: ``` docker run \ --gpus all --runtime=nvidia --privileged \ -it --rm -u 0:0 \ --shm-size=256g \ --ulimit memlock=-1 --ulimit stack=67108864 \ --ipc=host --network=host \ -v /tmp/.cache/huggingface:/root/.cache/huggingface \ --entrypoint /bin/bash \ vllm/vllm-openai:latest ``` reproduce the bug: on Spark: Qwen/Qwen3.5-122B-A10B-GPTQ-Int4 ``` sync && echo 3 | tee /proc/sys/vm/drop_caches && \ vllm bench throughput \ --model=Qwen/Qwen3.5-122B-A10B-GPTQ-Int4 \ --trust-remote-code --load-format=dummy \ --num-prompts=32 --output-len=256 --input-len=256 \ --quantization=gptq_marlin --kv-cache-dtype=auto \ --gpu-memory-utilization=0.85 --max-model-len=2048 \ --max-num-batched-tokens=2048 --max-num-seqs=512 \ --attention-backend=flashinfer \ --tensor-parallel-size=1 ``` RedHatAI/Qwen3.5-122B-A10B-NVFP4 ``` sync && echo 3 | tee /proc/sys/vm/drop_caches && \ vllm bench throughput \ --model=RedHatAI/Qwen3.5-122B-A10B-NVFP4 \ --tokenizer=Qwen/Qwen3.5-122B-A10B \ --trust-remote-code --load-format=dummy \ --num-prompts=32 --output...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: Buffer overflow when allocating memory error on Qwen3.5-122B-A10B-GPTQ-Int4 and NVFP4 bug ### Your current environment ### 🐛 Describe the bug The bug can be safely reproduce on Spark, B100 and B200(single GPU dev...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: be safely reproduce on Spark, B100 and B200(single GPU device) on latest build(v0.19.1) pull the image: ``` docker run \ --gpus all --runtime=nvidia --privileged \ -it --rm -u 0:0 \ --shm-size=256g \ --ulimit memlock=-1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: # 🐛 Describe the bug The bug can be safely reproduce on Spark, B100 and B200(single GPU device) on latest build(v0.19.1) pull the image: ``` docker run \ --gpus all --runtime=nvidia --privileged \ -it --rm -u 0:0 \ --sh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: 048 \ --max-num-batched-tokens=2048 --max-num-seqs=512 \ --attention-backend=flashinfer \ --tensor-parallel-size=1 ``` RedHatAI/Qwen3.5-122B-A10B-NVFP4 ``` sync && echo 3 | tee /proc/sys/vm/drop_caches && \ vllm bench t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: : Buffer overflow when allocating memory error on Qwen3.5-122B-A10B-GPTQ-Int4 and NVFP4 bug ### Your current environment ### 🐛 Describe the bug The bug can be safely reproduce on Spark, B100 and B200(single GPU device)...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
