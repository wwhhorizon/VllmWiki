# vllm-project/vllm#6805: [New Model]: Adding MiniGPT4_video model 

| 字段 | 值 |
| --- | --- |
| Issue | [#6805](https://github.com/vllm-project/vllm/issues/6805) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Adding MiniGPT4_video model 

### Issue 正文摘录

### The model to consider. Github code :https://github.com/Vision-CAIR/MiniGPT4-video huggingface demo : https://huggingface.co/spaces/Vision-CAIR/MiniGPT4-video huggingface package : https://huggingface.co/Vision-CAIR/MiniGPT4-video-llama-hf example of using huggingface package ```python from transformers import AutoModel video_path="path/to/the/video" instruction="Write your question here" use_subtitles=True minigpt4_video_obj=AutoModel.from_pretrained("Vision-CAIR/MiniGPT4-video-llama-hf",trust_remote_code=True) minigpt4_video_obj.to("cuda") minigpt4_video_obj.eval() answer=minigpt4_video_obj.inference_fun(video_path,instruction,use_subtitles) print(answer) ``` ### The closest model vllm already supports. [meta-llama/Llama-2-70b-hf](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llama.py) ### What's your difficulty of supporting the model you want? there are no new parts, but it is hard for me to integrate with vllm, I read the tutorial but can't do it. Your help in that will be greatly appreciated, as vllm is a very great framework for inference. Also, this project is based on MiniGPT4 for images , which also will be great if integrated with vllm htt...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Adding MiniGPT4_video model new-model;stale ### The model to consider. Github code :https://github.com/Vision-CAIR/MiniGPT4-video huggingface demo : https://huggingface.co/spaces/Vision-CAIR/MiniGPT4-video h
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: a-hf example of using huggingface package ```python from transformers import AutoModel video_path="path/to/the/video" instruction="Write your question here" use_subtitles=True minigpt4_video_obj=AutoModel.from_pretraine...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /MiniGPT4-video-llama-hf",trust_remote_code=True) minigpt4_video_obj.to("cuda") minigpt4_video_obj.eval() answer=minigpt4_video_obj.inference_fun(video_path,instruction,use_subtitles) print(answer) ``` ### The closest m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Adding MiniGPT4_video model new-model;stale ### The model to consider. Github code :https://github.com/Vision-CAIR/MiniGPT4-video huggingface demo : https://huggingface.co/spaces/Vision-CAIR/MiniGPT4-video...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: trust_remote_code=True) minigpt4_video_obj.to("cuda") minigpt4_video_obj.eval() answer=minigpt4_video_obj.inference_fun(video_path,instruction,use_subtitles) print(answer) ``` ### The closest model vllm already supports...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
