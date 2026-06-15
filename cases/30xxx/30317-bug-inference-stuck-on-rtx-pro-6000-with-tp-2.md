# vllm-project/vllm#30317: [Bug]: Inference stuck on RTX PRO 6000 with TP=2

| 字段 | 值 |
| --- | --- |
| Issue | [#30317](https://github.com/vllm-project/vllm/issues/30317) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inference stuck on RTX PRO 6000 with TP=2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The test script I used: ```bash export CUDA_VISIBLE_DEVICES=2,3 export NCCL_P2P_DISABLE=1 vllm serve /data/pretrain_models/Qwen3-8B \ --host localhost \ --port 20001 \ --trust-remote-code \ --tensor-parallel-size 2 \ --max-model-len 8192 \ --gpu-memory-utilization 0.9 \ ``` Test: ```bash vllm bench serve \ --backend vllm \ --endpoint /v1/completions \ --model /data/pretrain_models/Qwen3-8B \ --dataset-name random \ --random-input 800 \ --random-output 100 \ --num-prompts 100 \ --request-rate 5 \ --host localhost \ --port 20001 \ ``` Reasoning got stuck with TP=2, but it can reason normally with a single GPU: ```text (vllm) xxx@xx:~$ bash run_bench.sh Namespace(subparser='bench', bench_type='serve', dispatch_function= , seed=0, num_prompts=100, dataset_name='random', no_stream=False, dataset_path=None, no_oversample=False, skip_chat_template=False, disable_shuffle=False, custom_output_len=256, spec_bench_output_len=256, spec_bench_category=None, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, sharegpt_output_len=None, blazedit_min_distance=0.0, blazedit_max_distance=1.0, random_input_len=800, random_output_len=...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: VISIBLE_DEVICES=2,3 export NCCL_P2P_DISABLE=1 vllm serve /data/pretrain_models/Qwen3-8B \ --host localhost \ --port 20001 \ --trust-remote-code \ --tensor-parallel-size 2 \ --max-model-len 8192 \ --gpu-memory-utilizatio...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: _function= , seed=0, num_prompts=100, dataset_name='random', no_stream=False, dataset_path=None, no_oversample=False, skip_chat_template=False, disable_shuffle=False, custom_output_len=256, spec_bench_output_len=256, sp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: gpu-memory-utilization 0.9 \ ``` Test: ```bash vllm bench serve \ --backend vllm \ --endpoint /v1/completions \ --model /data/pretrain_models/Qwen3-8B \ --dataset-name random \ --random-input 800 \ --random-output 100 \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cache;cuda...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Inference stuck on RTX PRO 6000 with TP=2 bug ### Your current environment ### 🐛 Describe the bug The test script I used: ```bash export CUDA_VISIBLE_DEVICES=2,3 export NCCL_P2P_DISABLE=1 vllm serve /data/pretrai...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
