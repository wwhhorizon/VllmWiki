# vllm-project/vllm#31771: [Performance]: VLLM performance degradation when comparing with Tensor RT

| 字段 | 值 |
| --- | --- |
| Issue | [#31771](https://github.com/vllm-project/vllm/issues/31771) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: VLLM performance degradation when comparing with Tensor RT

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Hi Team, I am testing Stack AI benchmark suits on VLLM with DGX system having H100 and GH200 cards. I am getting 50% lower performance as compare to stack report with Tensor RT. Has anyone found this issue ? or Am I missing something related to optimization flag in vLLM. Vllm container bringup (snip from Stack AI Makefile): L318Bm10K: token=`cat hfToken`; \ docker run -d \ --runtime nvidia \ -e HUGGING_FACE_HUB_TOKEN=$$token \ -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ -e HTTPS_PROXY="$(HTTPS_PROXY)" \ --gpus '"device=$(GPUS)"' \ -p $(PORT):8000 \ -v $(CACHE):/root/.cache/huggingface \ --ipc=host \ $(CONTAINER) \ --model $(NVDFP8L318B) \ --disable-log-requests \ --gpu-memory-utilization 0.95 \ --kv-cache-dtype fp8 \ --async-scheduling \ --no-enable-prefix-caching \ --max-num-seqs 512 \ --max-num-batched-tokens 7168 \ --max-model-len 10000 docker ps ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for rel...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: gup (snip from Stack AI Makefile): L318Bm10K: token=`cat hfToken`; \ docker run -d \ --runtime nvidia \ -e HUGGING_FACE_HUB_TOKEN=$$token \ -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ -e HTTPS_PROXY="$(HTTPS_P...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: root/.cache/huggingface \ --ipc=host \ $(CONTAINER) \ --model $(NVDFP8L318B) \ --disable-log-requests \ --gpu-memory-utilization 0.95 \ --kv-cache-dtype fp8 \ --async-scheduling \ --no-enable-prefix-caching \ --max-num-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: m, I am testing Stack AI benchmark suits on VLLM with DGX system having H100 and GH200 cards. I am getting 50% lower performance as compare to stack report with Tensor RT. Has anyone found this issue ? or Am I missing s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ontainer bringup (snip from Stack AI Makefile): L318Bm10K: token=`cat hfToken`; \ docker run -d \ --runtime nvidia \ -e HUGGING_FACE_HUB_TOKEN=$$token \ -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ -e HTTPS_PRO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: : VLLM performance degradation when comparing with Tensor RT performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Hi Team, I am testing Stack AI benchmark suits on VLL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
