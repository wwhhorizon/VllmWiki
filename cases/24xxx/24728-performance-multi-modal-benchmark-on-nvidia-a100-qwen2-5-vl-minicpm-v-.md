# vllm-project/vllm#24728: [Performance]: Multi-Modal Benchmark on NVIDIA A100 – Qwen2.5-VL / MiniCPM-V-4 / InternVL3_5-4B / InternVL3_5-2B

| 字段 | 值 |
| --- | --- |
| Issue | [#24728](https://github.com/vllm-project/vllm/issues/24728) |
| 状态 | open |
| 标签 | performance;keep-open |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Multi-Modal Benchmark on NVIDIA A100 – Qwen2.5-VL / MiniCPM-V-4 / InternVL3_5-4B / InternVL3_5-2B

### Issue 正文摘录

### Proposal to improve performance ### Performance Bottleneck in Video Inference My tests indicate a significant performance bottleneck when processing multi-frame video inputs with vLLM. * **High Time-to-First-Token (TTFT):** In the Prefill Stage, vLLM encodes all frames of the entire video before generating the first text token. For long videos, this results in an extremely high Time-to-First-Token (TTFT) and a significant peak GPU memory footprint[cite: 9]. * **CPU Bottleneck & GPU Underutilization:** Test results on an NVIDIA A100 GPU show that when processing video, CPU utilization can spike to 100%, while GPU utilization remains at only about 20%. This indicates that video frame decoding and ViT feature extraction on the CPU side become bottlenecks, leading to idle GPU computing. * **Performance Comparison (Qwen2.5-VL-7B on 1xA100):** * **Single Image Input:** Generates responses at an average speed of approximately 132 tokens/s. * **Multi-frame (~30) Video Input:** The average generation speed drops to only about 10 tokens/s. ### Proposal: Streaming/Chunk-level Vision Encoding To address this issue, I propose implementing **Streaming or Chunk-level Vision Encoding**. Inste...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: [Performance]: Multi-Modal Benchmark on NVIDIA A100 – Qwen2.5-VL / MiniCPM-V-4 / InternVL3_5-4B / InternVL3_5-2B performance;keep-open ### Proposal to improve performance ### Performance Bottleneck in Video Inference My...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: Multi-Modal Benchmark on NVIDIA A100 – Qwen2.5-VL / MiniCPM-V-4 / InternVL3_5-4B / InternVL3_5-2B performance;keep-open ### Proposal to improve performance ### Performance Bottleneck in Video Inference My...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: lowed-local-media-path pathToData/datasets/ShareGPT4Video --port 8000 --dtype bfloat16 vllm bench serve --backend openai-chat --model Qwen/Qwen2.5-VL-7B-Instruct --dataset-name sharegpt --dataset-path pathToData/dataset...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Performance]: Multi-Modal Benchmark on NVIDIA A100 – Qwen2.5-VL / MiniCPM-V-4 / InternVL3_5-4B / InternVL3_5-2B performance;keep-open ### Proposal to improve performance ### Performance Bottleneck in Video Inference My...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: h Time-to-First-Token (TTFT) and a significant peak GPU memory footprint[cite: 9]. * **CPU Bottleneck & GPU Underutilization:** Test results on an NVIDIA A100 GPU show that when processing video, CPU utilization can spi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
