# vllm-project/vllm#17226: [Doc]: multi-image batch inference

| 字段 | 值 |
| --- | --- |
| Issue | [#17226](https://github.com/vllm-project/vllm/issues/17226) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: multi-image batch inference

### Issue 正文摘录

### 📚 The doc issue Can the official provide a batch inference script for multiple images? for example： questions = ["What are the contents of these pictures? Chinese answer", "Please compare the similarities and differences of the photos in detail. The answer must not be less than 100 words"] image_urls_list = [ ["/data5/home/pjwang/vllm/solifgeo/multi_image_1.jpeg", "/data5/home/pjwang/vllm/solifgeo/multi_image_2.jpeg", "/data5/home/pjwang/vllm/solifgeo/multi_image_3.jpeg", "/data5/home/pjwang/vllm/solifgeo/visual_grounding_1.jpeg"], ["/data5/home/pjwang/vllm/solifgeo/visual_grounding_2.jpg", "/data5/home/pjwang/vllm/solifgeo/visual_grounding_3.png"] ] I don't know how to use vllm for batch reasoning in this multi-modal multi-graph. Can the official provide a simple reasoning example code? ### Suggest a potential alternative/fix I don't know how to use vllm for batch reasoning in this multi-modal multi-graph. Can the official provide a simple reasoning example code? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lti-image batch inference documentation ### 📚 The doc issue Can the official provide a batch inference script for multiple images? for example： questions = ["What are the contents of these pictures? Chinese answer", "Pl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: de? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
