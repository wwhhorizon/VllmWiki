# vllm-project/vllm#39919: [Bug]: DeepSeek OCR doesn't work on vllm 0.19

| 字段 | 值 |
| --- | --- |
| Issue | [#39919](https://github.com/vllm-project/vllm/issues/39919) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek OCR doesn't work on vllm 0.19

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, I would like to report failure of vllm image with version 0.19 for DeepSeek OCR model. Host doesn't seem to matter here - I ran it on different linux machines all had Ubuntu or Nvidia's DGX Spark OS installed, architectures were amd or arm64. Models itself seems to be working fine, it works on every version older than latest (0.18, 0.17, 0.16). After updating vllm docker image to v0.19 (every time the same model is loaded locally, so no change in model here) deepseek starts throwing gibberish output. I provided small lorem ipsum image in replication, the smaller the image, the less problems with output, but they are still clrearly visible - sometimes alphabets are mixed (part of answer in Russian, part in Japanese), sometimes I get just random letters, sometimes parts of some non-existing on my machine documents (like Bible, Shakespeare or some public order documents) are being outputted, sometimes it's just some random prefix at the beginning, but 90% of the time there is output completely unrelated to input. This is small png image, you can upload anything bigger of your choice and problem will be more visible. It seems...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: cribe the bug Hello, I would like to report failure of vllm image with version 0.19 for DeepSeek OCR model. Host doesn't seem to matter here - I ran it on different linux machines all had Ubuntu or Nvidia's DGX Spark OS...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ferent linux machines all had Ubuntu or Nvidia's DGX Spark OS installed, architectures were amd or arm64. Models itself seems to be working fine, it works on every version older than latest (0.18, 0.17, 0.16). After upd...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ost 0.0.0.0 \ --port 8000 \ --gpu-memory-utilization 0.3 \ --dtype float16 \ --trust-remote-code curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d "{ \"model\": \"/models/DeepSeek-OCR...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: like to report failure of vllm image with version 0.19 for DeepSeek OCR model. Host doesn't seem to matter here - I ran it on different linux machines all had Ubuntu or Nvidia's DGX Spark OS installed, architectures wer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
