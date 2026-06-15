# vllm-project/vllm#17775: [Bug]: qwen2.5vl internal server error when processing videos from split_video_ffmpeg after realease 0.8.3

| 字段 | 值 |
| --- | --- |
| Issue | [#17775](https://github.com/vllm-project/vllm/issues/17775) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen2.5vl internal server error when processing videos from split_video_ffmpeg after realease 0.8.3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to use scenedetect to split video into small slices e.g. :split_video_ffmpeg(video_path, scene_list, output_dir=output_dir, show_progress=True, show_output=True) And I found out vllm can deal with original video but not those slice of videos. The log report says: vllm/multimodal/video.py", line 174, in load_bytes | assert i == num_frames | | AssertionError I went to the source code and found out that code was added in realease 0.8.3 ![Image](https://github.com/user-attachments/assets/461b57f6-cdeb-4316-897e-70a6d5386d41) So I install vllm==0.7.3 instead and it solves that problem, that is the code of 0.7.3 ![Image](https://github.com/user-attachments/assets/254a4b6c-82b7-43ea-84dc-709f524c1502) Please check that case, thankyou very much! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### 🐛 Describe the bug I tried to use scenedetect to split video into small slices e.g. :split_video_ffmpeg(video_path, scene_list, output_dir=output_dir, show_progress=True, show_output=True) And I found out vllm can d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen2.5vl internal server error when processing videos from split_video_ffmpeg after realease 0.8.3 bug ### Your current environment ### 🐛 Describe the bug I tried to use scenedetect to split video into small sli...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: .com/user-attachments/assets/461b57f6-cdeb-4316-897e-70a6d5386d41) So I install vllm==0.7.3 instead and it solves that problem, that is the code of 0.7.3 ![Image](https://github.com/user-attachments/assets/254a4b6c-82b7...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
