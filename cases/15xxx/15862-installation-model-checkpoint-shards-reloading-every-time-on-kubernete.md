# vllm-project/vllm#15862: [Installation]: Model checkpoint shards reloading every time on Kubernetes with vLLM image (even if already downloaded)

| 字段 | 值 |
| --- | --- |
| Issue | [#15862](https://github.com/vllm-project/vllm/issues/15862) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Model checkpoint shards reloading every time on Kubernetes with vLLM image (even if already downloaded)

### Issue 正文摘录

### Your current environment ```text I am using the latest vLLM image on Kubernetes, and I'm facing an issue where the "Loading safetensors checkpoint shards" process runs every time I restart the pod, even when the model is already cached locally. This leads to significant delays as the system repeatedly loads the safetensors from the cache, even though they should already be available for immediate use. Steps to Reproduce: Deploy the vLLM image on Kubernetes. Specify the following command arguments: args: - --model - /root/.cache/huggingface/hub/model70B/snapshot/28/ - --gpu-memory-utilization - "0.9" - --tensor-parallel-size - "8" - --enforce-eager - --load-format - safetensors - --max-parallel-loading-workers - "8" - --max-num-batched-tokens - "1024" - --block-size - "64" - --max-seq-len-to-capture - "2048" Restart the pod. Observe that the model checkpoint shards are reloaded, even though the model is already cached at /root/.cache/huggingface/hub/model70B/snapshot/28/. Expected Behavior: Once the model has been downloaded and cached, it should not need to reload the checkpoint shards each time the pod restarts, as they are already stored in the cache. The system should ideal...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Installation]: Model checkpoint shards reloading every time on Kubernetes with vLLM image (even if already downloaded) installation ### Your current environment ```text I am using the latest vLLM image on Kubernetes, a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: Model checkpoint shards reloading every time on Kubernetes with vLLM image (even if already downloaded) installation ### Your current environment ```text I am using the latest vLLM image on Kubernetes, a
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ven though they should already be available for immediate use. Steps to Reproduce: Deploy the vLLM image on Kubernetes. Specify the following command arguments: args: - --model - /root/.cache/huggingface/hub/model70B/sn...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: el-loading-workers - "8" - --max-num-batched-tokens - "1024" - --block-size - "64" - --max-seq-len-to-capture - "2048" Restart the pod. Observe that the model checkpoint shards are reloaded, even though the model is alr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
