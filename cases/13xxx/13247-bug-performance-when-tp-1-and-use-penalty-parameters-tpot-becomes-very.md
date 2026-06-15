# vllm-project/vllm#13247: [Bug]: [Performance] when tp=1 and use penalty parameters, TPOT becomes very slow for batch sizes > 20

| 字段 | 值 |
| --- | --- |
| Issue | [#13247](https://github.com/vllm-project/vllm/issues/13247) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | activation;attention;cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Performance] when tp=1 and use penalty parameters, TPOT becomes very slow for batch sizes > 20

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In vLLM v0.7.2 (same issue on v0.6.2), when tp=1 and calling api with penalty parameters, TPOT becomes very slow for batch sizes >= 20. (both A100 and H100 GPUs.) The vLLM arguments are as follows. ``` --model - /data/models/llama-3-8b-instruct/base --tensor-parallel-size - “1” --load-format - “auto” --max-model-len - “8192” --disable-log-requests --uvicorn-log-level - “warning” image: aspcr01-queffmyz.scr.skr-west.scp-in.com/serving/vllm:v0.7.2 ``` This works fine up to vLLM v0.6.0, but with v0.6.2~v0.7.2, there is an performance issue. The load scenario is as follows - Increase 10 users every minute - Each user requests 2,000 input tokens and 200 output tokens once every 10 seconds. Here is a table comparing the results. (test scenario is exactly same.) - In v0.6.0, CPU core usage is less than 2 cores and GPU utilization is close to 100%. - In v0.6.2/v0.7.2, CPU core usage rises to 4 cores (the maximum allocated to the pod), and GPU utilization is not high. | vLLM v0.6.0 | | | | vLLM v0.6.2~v0.7.2 | | | | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- Users | TPM(generated, K) | TPOT | cpu_usage | gpu_util(%) | TPM(generated,...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 6: d (vllm/utils.py) 0.00% 0.00% 1.20s 1.20s _get_graph_runner_block_tables (vllm/attention/backends/flash_attn.py) 0.00% 0.00% 1.00s 1.00s _random_sample (vllm/model_executor/layers/sampler.py) 0.00% 0.00% 0.700s 0.700s _...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: oth A100 and H100 GPUs.) The vLLM arguments are as follows. ``` --model - /data/models/llama-3-8b-instruct/base --tensor-parallel-size - “1” --load-format - “auto” --max-model-len - “8192” --disable-log-requests --uvico...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: - “auto” --max-model-len - “8192” --disable-log-requests --uvicorn-log-level - “warning” image: aspcr01-queffmyz.scr.skr-west.scp-in.com/serving/vllm:v0.7.2 ``` This works fine up to vLLM v0.6.0, but with v0.6.2~v0.7.2,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rofiled python process through py-spy. when concurrent user = 20, latencies start to go high. GIL is so high (71.43%) Unlike under normal circumstances, the make_tensor_with_pad method is very heavily utilized. ```bash...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: penalty parameters, TPOT becomes very slow for batch sizes >= 20. (both A100 and H100 GPUs.) The vLLM arguments are as follows. ``` --model - /data/models/llama-3-8b-instruct/base --tensor-parallel-size - “1” --load-for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
