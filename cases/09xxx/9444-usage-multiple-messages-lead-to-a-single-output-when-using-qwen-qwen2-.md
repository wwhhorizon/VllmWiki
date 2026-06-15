# vllm-project/vllm#9444: [Usage]: multiple messages lead to a single output when using `Qwen/Qwen2-VL-2B-Instruct`

| 字段 | 值 |
| --- | --- |
| Issue | [#9444](https://github.com/vllm-project/vllm/issues/9444) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: multiple messages lead to a single output when using `Qwen/Qwen2-VL-2B-Instruct`

### Issue 正文摘录

### Your current environment Same as https://github.com/vllm-project/vllm/issues/9128. ### Model Input Dumps _No response_ ### 🐛 Describe the bug This is basically a continuation of https://github.com/vllm-project/vllm/issues/9128. My code is: ```py from vllm import LLM, SamplingParams from decord import VideoReader, cpu from PIL import Image import base64 import io from huggingface_hub import hf_hub_download NUM_MAX_FRAMES = 4 BATCH_SIZE = 2 def encode_image(image): buffered = io.BytesIO() image.save(buffered, format="JPEG") image_bytes = buffered.getvalue() return base64.b64encode(image_bytes).decode("utf-8") def load_video(num_max_frames=4): video_filepath = hf_hub_download( repo_id="huggingface/documentation-images", repo_type="dataset", filename="diffusers/hiker.mp4" ) vr = VideoReader(video_filepath, ctx=cpu(0)) video_frames = [Image.fromarray(vr[i].asnumpy()) for i in range(len(vr))][:num_max_frames] return video_frames if __name__ == "__main__": # Use a limit of 4 frames. vllm_engine = LLM("Qwen/Qwen2-VL-2B-Instruct", limit_mm_per_prompt={"image": BATCH_SIZE * NUM_MAX_FRAMES}) sampling_params = SamplingParams(max_tokens=120) # Video. video_frames = load_video(num_max_frame...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: multiple messages lead to a single output when using `Qwen/Qwen2-VL-2B-Instruct` usage ### Your current environment Same as https://github.com/vllm-project/vllm/issues/9128. ### Model Input Dumps _No response_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: github.com/vllm-project/vllm/issues/9128. My code is: ```py from vllm import LLM, SamplingParams from decord import VideoReader, cpu from PIL import Image import base64 import io from huggingface_hub import hf_hub_downl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: age_bytes = buffered.getvalue() return base64.b64encode(image_bytes).decode("utf-8") def load_video(num_max_frames=4): video_filepath = hf_hub_download( repo_id="huggingface/documentation-images", repo_type="dataset", f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
