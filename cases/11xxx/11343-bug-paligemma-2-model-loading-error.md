# vllm-project/vllm#11343: [Bug]: Paligemma 2 model loading error

| 字段 | 值 |
| --- | --- |
| Issue | [#11343](https://github.com/vllm-project/vllm/issues/11343) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Paligemma 2 model loading error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are trying to make an inference with PaliGemma2 but getting the following error. Inference code we are using: ``` from vllm import LLM from vllm.assets.image import ImageAsset def run_paligemma(): llm = LLM(model="google/paligemma2-3b-ft-docci-448") prompt = "caption es" image = ImageAsset("image").pil_image outputs = llm.generate({ "prompt": prompt, "multi_modal_data": { "image": image }, }) for o in outputs: generated_text = o.outputs[0].text print(generated_text) if __name__ == "__main__": run_paligemma() ``` And following is the bug: ``` oading safetensors checkpoint shards: 0% Completed | 0/2 [00:00 [rank0]: run_paligemma() [rank0]: File "/pfs/lustrep4/projappl/project_465001347/caption-relabeling/test.py", line 6, in run_paligemma [rank0]: llm = LLM(model="google/paligemma2-3b-ft-docci-448") [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/opt/miniconda3/envs/pytorch/lib/python3.12/site-packages/vllm/utils.py", line 1140, in inner [rank0]: return fn(*args, **kwargs) [rank0]: ^^^^^^^^^^^^^^^^^^^ [rank0]: File "/opt/miniconda3/envs/pytorch/lib/python3.12/site-packa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Paligemma 2 model loading error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are trying to make an inference with PaliGemma2 but getting the following error...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: etting the following error. Inference code we are using: ``` from vllm import LLM from vllm.assets.image import ImageAsset def run_paligemma(): llm = LLM(model="google/paligemma2-3b-ft-docci-448") prompt = "caption es"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Paligemma 2 model loading error bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug We are trying to make an inference with PaliGemma2 but getting the following error...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
