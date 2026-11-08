# Professional motion: decisions, exercises and evidence

Read with the animation-principles skill for physical realism or a quality rebuild.
This is production guidance, not a claim that reading a document trains a model or
establishes professional-quality output. Demonstrate the decisions in the shot.

## 1. Mechanics before decorative easing

- Declare units, scale, gravity, body type, support, initial conditions and constraints.
  A dynamic body responds to forces; an authored/kinematic object follows a commanded
  path. Explain who/what drives a moving utensil rather than treating an unexplained
  floating prop as physical motion.
- Use position, velocity and acceleration deliberately. Free flight under constant
  gravity is parabolic. Starting, braking, contact and release need appropriate changes
  of velocity. A generic ease-in-out on every property erases the difference.
- Mass/inertia affect response to a given force/torque. Mass alone does not make a body
  fall more slowly or look heavy. Show weight through acceleration, contact, load,
  momentum transfer and settling. A contact force requires collision geometry/support.
- Friction opposes relative tangential motion; restitution controls normal rebound.
  Damping is not a replacement for contact friction. Avoid unexplained energy growth,
  arbitrary elastic bounces and constant-speed sliding without a driver.
- For unforced linear springs, use m*x'' + c*x' + k*x = 0 and
  zeta = c/(2*sqrt(k*m)). zeta=1 is critical damping, >1 overdamping, <1 underdamping.
  Choose a response for the material and event, not a blanket “premium” spring preset.

**Exercise:** supported object, release, flight, impact and settle. Record settings,
trajectory and contact times. Compare a few reference frames and velocity trends.
For numerical simulation fix the timestep/substeps, bake once and render the cache;
check thin/fast objects for tunneling and false contacts. Do not claim a calibrated
scientific experiment from an illustrative solver setup.

## 2. Body mechanics and manipulation

- Use consistent pivots and local/world coordinate spaces. Preserve limb lengths;
  solve joint chains within their reachable workspace and retain the intended elbow
  side. A 2D cap hiding a gap does not repair a broken chain.
- Establish balance and support before reach/lift. Planted feet belong to the ground
  space; a held prop belongs to the hand/constraint space until release. Preserve the
  grip offset as both move. Change parent/constraint without a world-space jump.
- Use preparation, arcs, follow-through and secondary motion where the action has a
  cause. Rigid tools held firmly need not lag behind the hand; loose sleeves/hair may.
- Distinguish frontal projection, pitch, yaw and roll. Tilting a portrait sideways
  does not demonstrate a bow. Review actual silhouette, contact and clearance.

**Exercise:** reach → establish grip → lift → place → release. Review dense frames
around each state change. Generated footage is subject to the same visible identity,
grip, support and object-permanence requirements; realistic texture cannot waive them.

## 3. Timing, spacing and staging

Write beats as events, with a focal subject and visible outcome. Use reference timing
and a dope sheet; inspect spacing as well as keyframe poses. Avoid identical durations,
identical easing or an automatic cut every few seconds across unrelated events.

Use anticipation when it clarifies intent, an accent at the important event, and a
settle/hold long enough to read the result. A purposeful still hold can improve rhythm;
random ambient motion does not rescue an uninteresting shot. Test the event muted
before depending on narration or sound to explain it.

**Exercise:** render three timings of the same action. Pick with an articulated reason
(weight, clarity, character intent, suspense), not an aggregate pixel-motion score.

## 4. Art direction is a separate craft

Choose a visual proposition: subject, audience, medium, palette, shape language,
material/line quality, lighting and reference intent. Build one style frame at final
aspect and useful resolution. Assess silhouette, proportion, detail hierarchy,
texture scale, edge treatment, negative space and type before animating a batch.

Primitive geometry is valid for blocking and intentional geometric design. A few
rounded rectangles and circles are not a finished human/food illustration merely
because joints move. Improve or replace the actual assets when the brief calls for
more craft. More polygons, realism, gradients or effects alone do not imply quality.

For 3D use material-appropriate roughness/reflection, coherent light directions,
contact shadows where visible and consistent scene scale. Depth of field, motion
blur and grain serve focus and photographic intent; they must not hide broken geometry.

## 5. Cinematography and edit

Pick focal length, viewpoint, subject scale and depth for a reason. Design clear action
silhouettes and screen direction. Let camera acceleration and stops have intent; avoid
constant orbiting, arbitrary zooms and camera motion that competes with the subject.

Cut on a motivated action or information change. Use wide/detail/insert/reaction
framings when useful, rather than enforcing a fixed shot count. Maintain axis, eyeline,
prop identity and spatial continuity when presenting continuous action. A match cut
cannot make a fork visibly morphing into a spoon acceptable inside the retained shot.

**Exercise:** a complete 5–10-second moving proof that includes the hardest contact,
changed framing and a readable outcome. Review the used interval and joins, not just
its nicest thumbnail. Save actual shot times, review method, failures and used trims.

## 6. Technique selection

| Production need | Suitable starting point | Frequent mismatch |
|---|---|---|
| Charts, labels, type, diagrams | Remotion + authored vector design | Springs and wipes standing in for a story |
| Layered illustration/characters | Designed assets + a real cutout/IK rig | Unfinished geometric people, detached joints |
| Weight, contact, mechanical objects | 3D scene + constrained/keyframed motion or baked physics | Floating objects and unvalidated collisions |
| Cinematic real-world scene | Permitted footage or suitable video generation + temporal QC | Beautiful stills with morphing props/hands |
| Premium product/tabletop film | Deliberate modeling/assets, materials, lighting, lenses and edited motion | An unlit orbit of a placeholder mesh |

Use installed tools first and inspect the actual runtime. Do not install or spend
because this table exists. A user requesting higher craft has not selected a provider.

## 7. Delivery gates and learning loop

Keep creative review separate from technical checks. Verify silhouette/contact/action,
staging, rhythm and designed asset quality; then verify decode, audio, captions and
deterministic export. A good ASR score does not validate pronunciation by a human, and
neither ASR nor ffprobe establishes visual craft.

After a rejected sample: identify the failure, choose a relevant exercise/technique,
render the moving proof, review it and record the decision. Do not scale the same weak
template into many more clips. Do not call reading references “trained,” or call an
agent-only technical pass “owner-approved.”

## Primary references

- [Pixar / Khan Academy: Pixar in a Box](https://www.pixar.com/pixar-in-a-box): a
  production-learning route connecting art, mathematics and filmmaking. Use the linked
  lessons that fit the exercise; the landing page is not proof of completed training.
- [Rapier rigid bodies](https://rapier.rs/docs/user_guides/javascript/rigid_bodies/):
  body types, forces, inertia, constraints and the need for attached colliders.
- [Rapier colliders](https://rapier.rs/docs/user_guides/javascript/colliders/):
  contact geometry, friction, restitution and supported collider behavior. API version
  must match the installed runtime before implementation.
- [Material motion](https://m3.material.io/styles/motion): interface motion guidance.
  Do not apply UI duration tokens as physical laws or fixed cinematic shot timing.
- BigO installed Blender/Cycles workflow: [three-d.md](../../../../content-studio/docs/three-d.md).
  Use its verified local runtime; inspect current Blender properties before scripting.
