# vllm-project/vllm#11191: [Installation]: Installing vllm in GH200 machine (aarch64) causes problems with cusparse.h missing

| 字段 | 值 |
| --- | --- |
| Issue | [#11191](https://github.com/vllm-project/vllm/issues/11191) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;kernel;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Installing vllm in GH200 machine (aarch64) causes problems with cusparse.h missing

### Issue 正文摘录

### Your current environment I cannot run collect_env.py since that would require vllm ### How you are installing vllm I am following the instructions from here: [https://docs.vllm.ai/en/stable/getting_started/installation.html#use-an-existing-pytorch-installation](https://docs.vllm.ai/en/stable/getting_started/installation.html?fbclid=IwZXh0bgNhZW0CMTAAAR0rKk7-u-dGjP9zdYYSFVpbj0REfhwjOhFgzrLC2DWeQDb5D1KbQFy-xLQ_aem_aEMTM-Po9v5WOAzcqzVmlg#use-an-existing-pytorch-installation) Problem I am facing: ``` pip install . --verbose --no-build-isolation Using pip 24.3.1 from /work/nvme/bcfp/ftajwar/anaconda3/envs/exploration/lib/python3.10/site-packages/pip (python 3.10) Processing /work/nvme/bcfp/ftajwar/vllm Running command Preparing metadata (pyproject.toml) running dist_info creating /tmp/pip-modern-metadata-nus2ddwg/vllm.egg-info writing /tmp/pip-modern-metadata-nus2ddwg/vllm.egg-info/PKG-INFO writing dependency_links to /tmp/pip-modern-metadata-nus2ddwg/vllm.egg-info/dependency_links.txt writing entry points to /tmp/pip-modern-metadata-nus2ddwg/vllm.egg-info/entry_points.txt writing requirements to /tmp/pip-modern-metadata-nus2ddwg/vllm.egg-info/requires.txt writing top-level names t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: Installing vllm in GH200 machine (aarch64) causes problems with cusparse.h missing installation;stale ### Your current environment I cannot run collect_env.py since that would require vllm ### How you
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: tallation.html?fbclid=IwZXh0bgNhZW0CMTAAAR0rKk7-u-dGjP9zdYYSFVpbj0REfhwjOhFgzrLC2DWeQDb5D1KbQFy-xLQ_aem_aEMTM-Po9v5WOAzcqzVmlg#use-an-existing-pytorch-installation) Problem I am facing: ``` pip install . --verbose --no-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: BLAS ... done. -- Building Marlin kernels for archs: 9.0 -- Building scaled_mm_c3x for archs: 9.0a;9.0 -- Not building scaled_mm_c2x as all archs are already built for and covered by scaled_mm_c3x -- Machete generation...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Installation]: Installing vllm in GH200 machine (aarch64) causes problems with cusparse.h missing installation;stale ### Your current environment I cannot run collect_env.py since that would require vllm ### How you ar...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tory: /work/nvme/bcfp/ftajwar/vllm/.deps -- CMake Version: 3.31.1 -- CUTLASS 3.5.1 -- CUDART: /opt/nvidia/hpc_sdk/Linux_aarch64/24.3/cuda/12.3/lib64/libcudart.so -- CUDA Driver: /opt/nvidia/hpc_sdk/Linux_aarch64/24.3/cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
