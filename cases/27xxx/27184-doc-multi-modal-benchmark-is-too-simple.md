# vllm-project/vllm#27184: [Doc]: Multi-Modal Benchmark is too simple

| 字段 | 值 |
| --- | --- |
| Issue | [#27184](https://github.com/vllm-project/vllm/issues/27184) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Multi-Modal Benchmark is too simple

### Issue 正文摘录

### 📚 The doc issue The latest doc about Multi-Modal Benchmark shows ： - 1、download sharegpt4v_instruct_gpt4-vision_cap100k.json and COCO's 2017 Train images - 2、vllm serve and vllm bench serve But there is so much details to concern: - 1、delete all json that not is coco`s in sharegpt4v_instruct_gpt4-vision_cap100k.json - 2、place COCO's 2017 Train images in /root directory like /train2017/, - 3、 vllm serve --allowed-local-media-path /train2017/ , because vllm use the condition: ``` if allowed_local_media_path not in filepath.resolve().parents ``` the ` filepath.resolve().parents` is ["/train2017", "/"], so the easiest‌ way is to place the images in /train2017/ and set `--allowed-local-media-path /train2017/` ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Doc]: Multi-Modal Benchmark is too simple documentation;stale ### 📚 The doc issue The latest doc about Multi-Modal Benchmark shows ： - 1、download sharegpt4v_instruct_gpt4-vision_cap100k.json and COCO's 2017 Train image...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: Multi-Modal Benchmark is too simple documentation;stale ### 📚 The doc issue The latest doc about Multi-Modal Benchmark shows ： - 1、download sharegpt4v_instruct_gpt4-vision_cap100k.json and COCO's 2017 Train image...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
