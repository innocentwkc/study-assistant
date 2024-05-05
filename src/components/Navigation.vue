<template>
  <div>
    <cds-header aria-label="IBM Platform Name">
      <cds-header-menu-button
        button-label-active="Close menu"
        button-label-inactive="Open menu"></cds-header-menu-button>
      <cds-header-name href="javascript:void 0" prefix="IBM"
        >[Platform]</cds-header-name
      >
      <cds-header-nav menu-bar-label="IBM [Platform]">
        <cds-header-nav-item href="javascript:void 0">Link 1</cds-header-nav-item>
        <cds-header-nav-item href="javascript:void 0">Link 2</cds-header-nav-item>
        <cds-header-nav-item href="javascript:void 0">Link 3</cds-header-nav-item>
        <cds-header-menu menu-label="Link 4" trigger-content="Link 4">
          <cds-header-menu-item href="javascript:void 0"
            >Sub-link 1</cds-header-menu-item
          >
          <cds-header-menu-item href="javascript:void 0"
            >Sub-link 2</cds-header-menu-item
          >
          <cds-header-menu-item href="javascript:void 0"
            >Sub-link 3</cds-header-menu-item
          >
        </cds-header-menu>
      </cds-header-nav>
    </cds-header>
    <cds-side-nav aria-label="Side navigation" expanded>
      <cds-side-nav-items>
        <cds-side-nav-menu title="Tools">
          <router-link active aria-current="page" class="" to="/pomodoro">
            Pomodoro
          </router-link>
          <router-link class="" to="/about">
            About
          </router-link>
          <cds-side-nav-menu-item  href="www.ibm.com">
            L0 menu item
          </cds-side-nav-menu-item>
          <cds-side-nav-menu-item href="www.ibm.com">
            L0 menu item
          </cds-side-nav-menu-item>
        </cds-side-nav-menu>
        <!-- <cds-side-nav-divider></cds-side-nav-divider> -->
        <cds-side-nav-link href="javascript:void(0)">L0 link</cds-side-nav-link>
        <cds-side-nav-link href="javascript:void(0)">L0 link</cds-side-nav-link>
      </cds-side-nav-items>
    </cds-side-nav>
  </div>
</template>