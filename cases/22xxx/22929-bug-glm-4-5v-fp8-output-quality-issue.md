# vllm-project/vllm#22929: [Bug]: GLM-4.5V-FP8 output quality issue

| 字段 | 值 |
| --- | --- |
| Issue | [#22929](https://github.com/vllm-project/vllm/issues/22929) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5V-FP8 output quality issue

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GLM-4.5V-FP8 generates garbage output while GLM-4.5V is ok - Repro script ``` import vllm from vllm import SamplingParams from vllm.lora.request import LoRARequest from vllm.config import CompilationConfig try: from vllm.utils import FlexibleArgumentParser except ImportError: from argparse import ArgumentParser as FlexibleArgumentParser MODEL= "zai-org/GLM-4.5V-FP8" QUESTION = "What is the content of each image?" IMAGE_URLS = [ "https://upload.wikimedia.org/wikipedia/commons/d/da/2015_Kaczka_krzy%C5%BCowka_w_wodzie_%28samiec%29.jpg", "https://upload.wikimedia.org/wikipedia/commons/7/77/002_The_lion_king_Snyggve_in_the_Serengeti_National_Park_Photo_by_Giles_Laurent.jpg", "https://upload.wikimedia.org/wikipedia/commons/2/26/Ultramarine_Flycatcher_%28Ficedula_superciliaris%29_Naggar%2C_Himachal_Pradesh%2C_2013_%28cropped%29.JPG", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Anim1754_-_Flickr_-_NOAA_Photo_Library_%281%29.jpg/2560px-Anim1754_-_Flickr_-_NOAA_Photo_Library_%281%29.jpg", "https://upload.wikimedia.org/wikipedia/commons/d/d4/Starfish%2C_Caswell_Bay_-_geograph.org.uk_-_409413.jpg", "https://upload.wikimedia.or...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .5V-FP8 generates garbage output while GLM-4.5V is ok - Repro script ``` import vllm from vllm import SamplingParams from vllm.lora.request import LoRARequest from vllm.config import CompilationConfig try: from vllm.uti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: GLM-4.5V-FP8 output quality issue bug;stale ### Your current environment ### 🐛 Describe the bug GLM-4.5V-FP8 generates garbage output while GLM-4.5V is ok - Repro script ``` import vllm from vllm import SamplingP...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mport SamplingParams from vllm.lora.request import LoRARequest from vllm.config import CompilationConfig try: from vllm.utils import FlexibleArgumentParser except ImportError: from argparse import ArgumentParser as Flex...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: pears to be calmly floating, with its body partially submerged, creating small waves around it." Generated text: " The user is asking to describe the content of the image. First, I need to look at the image carefully. T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: GLM-4.5V-FP8 output quality issue bug;stale ### Your current environment ### 🐛 Describe the bug GLM-4.5V-FP8 generates garbage output while GLM-4.5V is ok - Repro script ``` import vllm from vllm import SamplingP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
